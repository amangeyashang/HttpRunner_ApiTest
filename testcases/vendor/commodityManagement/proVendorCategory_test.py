# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/23 17:07'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("删除分类")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("删除分类-001")
            .with_variables(**{})
            .post("/proVendorCategory/delete")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "id":"7",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","该分类下还有商品,不能删除")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()