# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/13 11:27'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("分页查询Spu")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("分页查询Spu-001")
            .with_variables(**{})
            .post("/spu/pageQuerySpu")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "categoryIdF":"",
                    "categoryIdS":"",
                    "categoryId":"",
                    "name":"",
                    "productCode":"",
                    "brandName":"",
                    "createTimeBegin":"",
                    "createTimeEnd":"",
                    "pageInfo":{"pageNo":1,"pageSize":10,"total":0},
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()