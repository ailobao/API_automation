# api/contract_api.py
import requests
import config
import random
from api.login_api import get_token

def contract_upload(token,**kwargs):
    headers = {}
    if token is not None:
        headers = {
            "Authorization": f"Bearer {token}"
        }
    file_path = kwargs.get('file_path')
    with open(file_path, 'rb') as f:
        files = {'file': f}
        resp = requests.post(
            f'{config.BASE_URL}{config.CONTRACT_UPLOAD}',
            headers=headers,
            files=files
        )
    return  resp.json()

def contract_add(token,**kwargs):
    headers = {}
    if token is not None:
        headers = {
            "Authorization": f"Bearer {token}"
        }
    params={}
    for key, value in kwargs.items():
        if value is not None:
            params[key] = value
    resp = requests.post(
        f'{config.BASE_URL}{config.CONTRACT_ADD}',
        headers=headers,
        json=params
    )
    return resp.json()

def get_contract_list(token,**kwargs):
    headers = {}
    if token is not None:
        headers = {
        "Authorization": f"Bearer {token}"
        }
    params = {}
    for key, value in kwargs.items():
        if value is not None:
            params[key] = value
    resp = requests.get(
        f'{config.BASE_URL}{config.CONTRACT_LIST}',
        headers=headers,
        params=params
    )
    return resp.json()

def get_contract_ids(token,**kwargs):
    result = get_contract_list(token, **kwargs)
    id_list = []
    for course in result.get("rows", []):
        course_id = course.get("id")
        if course_id is not None:
            id_list.append(course_id)
    return id_list


def contract_remove(token, **kwargs):
    """删除合同"""
    contract_id = kwargs.get("id")

    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = {"id": contract_id}

    resp = requests.post(
        f'{config.BASE_URL}{config.CONTRACT_REMOVE}',
        headers=headers,
        data=data
    )
    try:
        return resp.json()
    except:
        # 无法解析 JSON，就包装成字典，code 用 HTTP 状态码
        return {"code": resp.status_code, "msg": resp.text}


if __name__ == '__main__':

    file_path = '../test.pdf'
    token = get_token()

    print("================= 合同上传 =================")
    upload_result = contract_upload(token, file_path=file_path)
    print(f"合同上传结果:\n{upload_result}\n")

    # 检查上传是否成功
    if upload_result and upload_result.get('code') == 200:
        file_name = upload_result.get('fileName')
    else:
        print("文件上传失败，终止后续操作")
        file_name = None

    if file_name:
        contract_data = {
            "name": "alobao",
            "phone": "13513531480",
            "contractNo": f"HT{random.randint(123456789, 999999999)}",
            "subject": "6",
            "courseId": 593253,
            "channel": "0",
            "activityId": 77,
            "fileName": file_name
        }

        print("================= 合同新增 =================")
        add_result = contract_add(token, **contract_data)
        print(f"合同新增结果:\n{add_result}\n")

        print("================= 合同查询 =================")
        list_result = get_contract_list(token, phone='13513531480')
        print(f"合同查询结果:\n{list_result}\n")

        print("================= 合同id列表查询 =================")
        ids_list = get_contract_ids(token, phone='13513531480')
        print(f"合同ID列表: {ids_list}")

        print("================= 合同删除 =================")
        if ids_list:
            # 删除最后一个合同
            contract_id = ids_list[-1]
            print(f"要删除的合同ID: {contract_id}")
            delete_result = contract_remove(token, id=contract_id)
            print(f"删除结果: {delete_result}")
        else:
            print("没有找到合同，跳过删除")
    else:
        print("上传失败，跳过合同新增和查询")
