# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 10:58'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from .getTemplate_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)#导入引用的类

class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取模版详情")
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("request with functions")
            .call(RequestWithFunctions)#导入后就可以调用了
            .export(*["templateId1","templateType1"])#在RunTestCase步骤中定义这个变量的导出
        ),
        Step(
            RunRequest("获取模板详情-001")
            .with_variables(**{})
            .post("/indexApiService/templateDetails")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "vendorCode": "${ENV(vendorCode)}",
                    "templateId": "$templateId1",
                    "advertisementType": "$templateType1"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()