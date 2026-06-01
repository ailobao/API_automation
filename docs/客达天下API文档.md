# 客达天下接口文档
- 系统基本路径：http://kdtx-test.itheima.net



## 登录

### 生成验证码
**PATH:** /api/captchaImage

**Type:** GET

**Description:** 生成验证码

**Response-example:**

响应状态码：200

响应数据：`{ "msg": "操作成功", "img": "......", "code": 200, "uuid": "xxxxxx"}`



### 登录

**URL:** /api/login

**Type:** POST

**Description:** 登录方法

**Request-header:**

| 参数名称         | 参数值           | 是否必填 | 示例 | 备注 |
| ---------------- | ---------------- | -------- | ---- | ---- |
| **Content-Type** | application/json | 是       |      |      |

**Body-parameters:**

参数名称 | 类型 |描述|是否必填|备注
---|---|---|---|---
username|string|用户名|True|如：manager
password|string|用户密码|True|如：123456
code|string|验证码|True| 如：2          
uuid|string|唯一标识|True|生成验证码接口

**Response:**

| 参数名称 | 类型   | 描述      | 是否必填 | 备注 |
| -------- | ------ | --------- | -------- | ---- |
| msg      | string | 消息      | True     |      |
| code     | int64  | 业务代码  | True     |      |
| token    | string | 令牌token | False    |      |

**Request-example:**

```json
{
    "username": "manager",
    "password": "123456",
    "code": "2",
    "uuid": "a5762bc30ec74055a58dba2c63b01087"
}
```

**Response-example:**

响应状态码：200

响应数据：

`①：登录成功：{ "msg": "操作成功", "code": 200, "token": "xxxxxx"}`

`② 用户名或密码错误：{ "msg": "用户名或密码错误", "code": 500}`

`③ 验证码错误或过期：{"msg": "验证码已失效", "code": 500}`



## 课程管理

### 新增课程

**URL:** /api/clues/course

**Type:** POST

**Description:** 新增课程管理

**Request-header:**

| 参数名称          | 参数值           | 是否必填 | 示例                            | 备注     |
| ----------------- | ---------------- | -------- | ------------------------------- | -------- |
| **Authorization** | token            | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |
| **Content-Type**  | application/json | 是       |                                 |          |

**Body-parameters:**

| Parameter        | Type   | Description | Required | Since |
| ---------------- | ------ | ----------- | -------- | ----- |
| name             | string | 课程名称    | True     | -     |
| subject          | string | 课程学科    | True     | -     |
| price            | int32  | 课程价格    | True     | -     |
| applicablePerson | string | 适用人群    | True     | -     |
| info             | string | 课程介绍    | false    | -     |

**Request-example:**

```json
{
    "name": "测试开发提升课01",
    "subject": "6",
    "price": 899,
    "applicablePerson": "2",
    "info": "测试开发提升课01"
}
```

**Response-example:**

响应状态码：200

响应数据：

① 添加成功：`{ "msg": "操作成功", "code": 200}`

② 未登录：`{ "msg": "请求访问：/clues/course，认证失败，无法访问系统资源", "code": 401}`

③ 添加失败：`{ "msg": "操作失败", "code": 500}`



### 查询课程列表

**URL:** /api/clues/course/list

**Type:** GET

**Description:** 查询课程管理列表

**Request-header:**

| 参数名称          | 参数值 | 是否必填 | 示例                            | 备注     |
| ----------------- | ------ | -------- | ------------------------------- | -------- |
| **Authorization** | token  | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |

**Query-parameters:**

| Parameter        | Type   | Description | Required | Since |
| ---------------- | ------ | ----------- | -------- | ----- |
| name             | string | 课程名称    | false    | -     |
| subject          | string | 课程学科    | false    | -     |
| price            | int32  | 课程价格    | false    | -     |
| applicablePerson | string | 适用人群    | false    | -     |
| info             | string | 课程介绍    | false    | -     |



**Response-example:**

响应状态码：200

响应数据：

①存在满足条件的课程信息：

```json
{
    "total": 1,
    "rows": [
        {
            "createTime": "2022-11-29 07:36:53",
            "id": 43,
            "name": "测试开发提升课01",
            "code": "nii59qtl",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01",
            "isDelete": 0
        }
    ],
    "code": 200,
    "msg": "查询成功"
}
```



② 不存在满足条件的课程信息：

```yacas
{
    "total": 0,
    "rows": [],
    "code": 200,
    "msg": "查询成功"
}
```



③ 不输入查询条件,显示默认数据

```yacas
{
    "total": 16,
    "rows": [
        {
            "createTime": "2022-12-01 00:57:15",
            "id": 75,
            "name": "测试开发提升课777",
            "code": "zem8nxp3",
            "subject": "6",
            "price": 5000,
            "applicablePerson": "2",
            "info": "测试开发提升课36",
            "isDelete": 0
        },
		......
    ],
    "code": 200,
    "msg": "查询成功"
}
```

④ 未登录：`{ "msg": "请求访问：/clues/course，认证失败，无法访问系统资源", "code": 401}`



### 查询课程

**URL:** /api/clues/course/:id

**Type:** GET

**Description:** 查询课程

**Request-header:**

| 参数名称          | 参数值 | 是否必填 | 示例                            | 备注     |
| ----------------- | ------ | -------- | ------------------------------- | -------- |
| **Authorization** | token  | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |

**Path-parameters:**

| Parameter | Description | Required | Since |
| --------- | ----------- | -------- | ----- |
| id        | 课程ID      | true     |       |

**Response-example:**

响应状态码：200

响应数据：

① 查询成功：

```json
{
    "msg": "操作成功",
    "code": 200,
    "data": {
        "createTime": "2023-12-23 03:40:04",
        "id": 1000127924,
        "name": "jack-postman-1223-001",
        "code": "ie4jmk8g",
        "subject": "6",
        "price": 899,
        "applicablePerson": "2",
        "info": "jack-postman-1223课01",
        "isDelete": 0
    }
}
```

② 未登录：`{ "msg": "请求访问：/clues/course/:id，认证失败，无法访问系统资源", "code": 401 }`



### 修改课程

**URL:** /api/clues/course

**Type:** PUT

**Description:** 修改课程管理

**Request-header:**

| 参数名称          | 参数值           | 是否必填 | 示例                            | 备注     |
| ----------------- | ---------------- | -------- | ------------------------------- | -------- |
| **Authorization** | token            | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |
| **Content-Type**  | application/json | 是       |                                 |          |

**Body-parameters:**

| Parameter        | Type   | Description  | Required | Since |
| ---------------- | ------ | ------------ | -------- | ----- |
| id               | int64  | 课程id       | True     | -     |
| name             | string | 课程名称     | false    | -     |
| subject          | string | 课程学科     | false    | -     |
| price            | int32  | 价格         | false    | -     |
| applicablePerson | string | 适用人群     | false    | -     |
| info             | string | 课程描述信息 | false    | -     |

**Request-example:**

```yacas
{
    "id": 93,
    "name": "接口测试001",
    "subject": "6",
    "price": 998,
    "applicablePerson": "2",
    "info": "课程介绍001"
}
```

**Response-example:**

响应状态码：200

响应数据：

① 修改成功：`{ "msg": "操作成功", "code": 200 }`

② 未登录：`{ "msg": "请求访问：/clues/course，认证失败，无法访问系统资源", "code": 401 }`

③ 修改失败：`{ "msg": "操作失败", "code": 500}`



### 删除课程

**URL:** /api/clues/course/:id

**Type:** DELETE

**Description:** 删除课程管理

**Request-header:**

| 参数名称          | 参数值 | 是否必填 | 示例                            | 备注     |
| ----------------- | ------ | -------- | ------------------------------- | -------- |
| **Authorization** | token  | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |

**Path-parameters:**

| Parameter | Description | Required | Since |
| --------- | ----------- | -------- | ----- |
| id        | 课程ID      | true     |       |

**Response-example:**

响应状态码：200

响应数据：

① 删除成功：`{ "msg": "操作成功", "code": 200 }`

② 未登录：`{ "msg": "请求访问：/clues/course/:id，认证失败，无法访问系统资源", "code": 401 }`

③ 删除失败：`{ "msg": "操作失败", "code": 500}`



## 合同管理

### 合同上传

**URL:** /api/common/upload

**Type:** POST

**Description:** 合同上传

**Request-header:**

| 参数名称          | 参数值              | 是否必填 | 示例                            | 备注     |
| ----------------- | ------------------- | -------- | ------------------------------- | -------- |
| **Authorization** | token               | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |
| **Content-Type**  | multipart/form-data | 是       |                                 |          |

**Body-parameters:**

| 参数名称 | 数据类型 | 参数值   | 是否必填 | Since |
| -------- | -------- | -------- | -------- | ----- |
| file     | string   | 文件路径 | true     |       |

**Response-example:**

响应状态码：200

响应数据：

```yacas
{
    "msg": "操作成功",
    "fileName": "/profile/upload/2023/01/05/0c8642af-4d79-47ca-8151-67e4f8921ca5.pdf",
    "code": 200,
    "url": "http://localhost:8080/profile/upload/2023/01/05/0c8642af-4d79-47ca-8151-67e4f8921ca5.pdf"
}
```



### 新增合同

**URL:** /api/contract

**Type:** POST

**Description:** 新增合同

**Request-header:**

| 参数名称          | 参数值           | 是否必填 | 示例                            | 备注     |
| ----------------- | ---------------- | -------- | ------------------------------- | -------- |
| **Authorization** | token            | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |
| **Content-Type**  | application/json | 是       |                                 |          |

**Body-parameters:**

| Parameter  | Type   | Description | Required | Since                      |
| ---------- | ------ | ----------- | -------- | -------------------------- |
| contractNo | string | 合同编号    | True     | -                          |
| phone      | string | 手机号      | True     | -                          |
| name       | string | 客户姓名    | True     | -                          |
| subject    | string | 意向学科    | True     | -                          |
| channel    | string | 渠道来源    | false    | 0：线上活动<br>1：推广介绍 |
| activityId | int64  | 活动信息    | false    | -                          |
| courseId   | int64  | 课程id      | True     | -                          |
| fileName   | string | 文件名称    | True     | -                          |

**Request-example:**

```yacas
{
    "name": "测试888",
    "phone": "13612341888",
    "contractNo": "HT10012004",
    "subject": "6",
    "courseId": 99,
    "channel": "0",
    "activityId": 77,
    "fileName": "/profile/upload/2023/01/05/86e5a3b8-b08c-470c-a17d-71375c3a8b9f.pdf"
}
```

**Response-example:**

响应状态码：200

响应数据：`{ "msg": "操作成功", "code": 200}`



### 查询合同列表

**URL:** /api/contract/list

**Type:** GET

**Description:** 查询合同列表

**Request-header:**

| 参数名称          | 参数值 | 是否必填 | 示例                            | 备注     |
| ----------------- | ------ | -------- | ------------------------------- | -------- |
| **Authorization** | token  | 是       | Bearer eyJhbGjgfjG2INQjIHFirwSw | 登录接口 |

**Query-parameters:**

| Parameter | Type   | Description | Required | Since |
| --------- | ------ | ----------- | -------- | ----- |
| phone     | string | 手机号      | false    | -     |

**Response-fields:**

| Field        | Type   | Description        | Since |
| ------------ | ------ | ------------------ | ----- |
| total        | int64  | 总记录数           | -     |
| rows         | array  | 列表数据           | -     |
| code         | int32  | 消息状态码         | -     |
| msg          | string | 消息内容           | -     |
| params       | map    | No comments found. | -     |
| └─any object | object | any object.        | -     |

**Response-example:**

响应状态码：200

响应数据：

```yacas
{
    "total": 1,
    "rows": [
        {
            "createBy": "admin",
            "createTime": "2023-01-05 08:58:51",
            "id": "7417444345987875",
            "contractNo": "HT10012004",
            "phone": "13612341888",
            "name": "测试888",
            "subject": "6",
            "channel": "0",
            "activityId": 77,
            "activityName": "代金券测试888",
            "courseId": 99,
            "courseName": "接口测试001",
            "status": "1",
            "fileName": "/profile/upload/2023/01/05/86e5ad-71375c3a8b9f.pdf",
            "coursePrice": 998.0,
            "discountType": "代金券",
            "order": 898.0,
            "deptId": 103
        }
    ],
    "code": 200,
    "msg": "查询成功"
}
```



### 删除合同

**URL:** /api/contract/remove

**Type:** POST

**Description:** 删除课程管理

**Request-header:**

| 参数名称          | 参数值                            | 是否必填 | 示例          | 备注     |
| ----------------- | --------------------------------- | -------- | ------------- | -------- |
| **Authorization** | token                             | 是       | Bearer xxxxxx | 登录接口 |
| **Content-Type**  | application/x-www-form-urlencoded |          |               |          |

**Body-parameters:**

| Parameter | Description | Required | Since |
| --------- | ----------- | -------- | ----- |
| id        | 合同id      | true     |       |

**Request-example:**

```yacas
{ "id": 10950251898105098 }
```

响应状态码：200

响应数据：

① 删除成功：`删除成功！`

② 未登录：`{ "msg": "请求访问：/contract/remove，认证失败，无法访问系统资源","code": 401}`

③ 删除失败：`删除失败！`

④ 删除失败：`缺少必填参数：id`