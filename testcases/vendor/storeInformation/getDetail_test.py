# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/12 11:09'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("店铺基础数据")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunRequest("店铺基础数据-001")
            .with_variables(**{})
            .get("/vendorRegister/getDetail")
            .with_params(
                **{
                    "vendorId":"${ENV(vendorId)}"
                }
            )
            .extract()
            .with_jmespath("body.data.id","vendorId")
            .with_jmespath("body.data.userId","sellerId")
            .with_jmespath("body.data.vendorName","vendorName")
            .with_jmespath("body.data.vendorCode","vendorCode")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()