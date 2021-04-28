# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/21 17:45'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.storeInformation.getDetail_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
from .pageQueryPurchaseOrder_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("根据采购单编号查询采购单明细")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId","orderNo"])
        ),
        Step(
            RunRequest("根据采购单编号查询采购单明细-001")
            .with_variables(**{})
            .post("/tob/purchaseOrderItem/getPurchaseProductItemByOrderNo")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "orderNo":"$orderNo",
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .extract()
            .with_jmespath("body.purchaseOrderItemInfoList[0].itemNo","itemNo")
            .with_jmespath("body.purchaseOrderItemInfoList[0].quantity","quantity")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.message","成功")
            .assert_equal("body.status","S")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()