# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:37'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("获取精选商品分类")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("获取精选商品分类-001")
            .with_variables(**{})
            .post("/indexApiService/getFeaturedProductsCategorys")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "vendorId": "${ENV(vendorId)}",
                    "vendorCode": "${ENV(vendorCode)}"

                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()