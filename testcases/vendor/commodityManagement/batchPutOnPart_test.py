# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 16:10'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("批量上下架商品")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("批量上下架商品-下架商品-001")
            .with_variables(**{})
            .post("/newVendorProduct/batchPutOnPart")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "all":'false',
                    "productIds":["694729859712307200","694663830504099840"],
                    "putway":'false',
                    "vendorId":"546520236057329664",
                    "memberId":"2501",
                    "userId":"2501",
                    "depotCode":"VC10003",
                    "vendorCode":"VC10003"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("批量上下架商品-上架商品-002")
                .with_variables(**{})
                .post("/newVendorProduct/batchPutOnPart")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "all":'false',
                    "productIds":["694729859712307200","694663830504099840"],
                    "putway":'true',
                    "vendorId":"546520236057329664",
                    "memberId":"2501",
                    "userId":"2501",
                    "depotCode":"VC10003",
                    "vendorCode":"VC10003"
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()