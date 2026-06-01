# api/course_api.py
import requests
import config
import conftest
from api.login_api import get_token


def course_add(token,**kwargs):
    """新增课程"""
    headers = {
        "Content-Type": "application/json",
    }
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    params={}
    for key,value in kwargs.items():
        if key is not None:
            params[key] = value
    resp = requests.post(f'{config.BASE_URL}{config.COURSE_ADD}',
                         headers=headers,json=params)
    return resp.json()



def get_course_list(token, **kwargs):
    """查询课程列表"""
    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    params={}
    for key,value in kwargs.items():
        if key is not None:
            params[key] = value
    
    resp = requests.get(
        f'{config.BASE_URL}{config.COURSE_LIST}',
        params=params,
        headers=headers
    )
    return resp.json()


def get_course_ids(token, **kwargs):
    """只获取课程ID列表"""
    result = get_course_list(token, **kwargs)

    id_list = []
    for course in result.get("rows", []):
        course_id = course.get("id")
        if course_id is not None:
            id_list.append(course_id)
    return id_list


def get_course_detail(token, **kwargs):
    """查询单个课程详情"""
    course_id =kwargs.get("course_id","")
    url = config.COURSE_DETAIL.replace(":id", str(course_id))
    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    for key, value in kwargs.items():
        if key is not None:
            params[key] = value

    resp = requests.get(f'{config.BASE_URL}{url}', headers=headers,params=params)
    return resp.json()

def course_update(token, **kwargs):
    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    data = {}
    for key, value in kwargs.items():
        if value is not None:
            data[key] = value
    resp = requests.put(f'{config.BASE_URL}{config.COURSE_UPDATE}',
                         headers=headers, json=data)
    return resp.json()


def course_delete(token, **kwargs):
    """删除单个课程"""
    course_id = kwargs.get("course_id", "")
    url = config.COURSE_DELETE.replace(":id", str(course_id))

    headers = {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    resp = requests.delete(f'{config.BASE_URL}{url}', headers=headers)
    return resp.json()




def delete_course_by_name(token, name=None):
    """按名称删除所有课程"""
    course_ids = get_course_ids(token, name=name)
    print(f"找到的课程ID: {course_ids}")

    for course_id in course_ids.copy():
        result = course_delete(token, course_id)
        if result.get("code") == 200:
            print(f"✓ 已删除课程ID: {course_id}")
        else:
            print(f"✗ 删除失败: {course_id}")

    print(f"删除完成，共处理 {len(course_ids)} 门课程")


if __name__ == '__main__':
    token = get_token()
    add_params = {
        "name": "天天开心好课程",
        "subject": "2",
        "price": 998,
        "applicablePerson": "2",
        "info": ""
    }

    # 1. 新增课程
    print("=== 新增课程 ===")
    add_result = course_add(token=token, **add_params)
    print(add_result)

    # 2. 查询列表
    print("\n=== 查询列表 ===")
    list_result = get_course_list(token=token, **{"name": "天天开心好课程"})
    print(list_result)

    # 3. 获取课程ID
    print("\n=== 获取课程ID ===")
    course_ids = get_course_ids(token, **add_params)
    print(f"课程ID列表: {course_ids}")

    # 4. 查询详情（如果有课程）
    if course_ids:
        print("\n=== 查询详情 ===")
        detail_result = get_course_detail(token=token, **{"course_id": course_ids[-1]})
        print(detail_result)

    # 5. 修改课程
        print("\n=== 修改课程 ===")
        update_result = course_update(
            token=token,
            id=course_ids[-1],
            name='天天开心好课程01',
            subject='3',
            info='这已经是更改过的了'
        )
        print(update_result)

        # 5. 删除课程

        print("\n=== 删除最新课程 ===")
        print(f'\n=== 删除前 ===\n{get_course_detail(token=token, **{"course_id": course_ids[-1]})}')
        delete_result = course_delete(token=token, **{"course_id": course_ids[-1]})
        print(delete_result)

        # 6. 验证删除（再次查询应该找不到）
        print("\n=== 验证删除 ===")
        detail_after = course_delete(token=token, **{"course_id": course_ids[-1]})
        print(detail_after)
    else:
        print("没有找到课程")



