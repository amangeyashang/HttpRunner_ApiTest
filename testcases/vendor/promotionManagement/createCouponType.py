# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/4/14 10:29'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.vendor.userControl.getMemberId_test import (TestCaseDemoTestcaseRequest as RequestWithFunctions)
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("创建优惠券")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_develop_vendor)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase("导出变量")
            .call(RequestWithFunctions)
            .export(*["vendorCode","sellerId","vendorId"])
        ),
        Step(
            RunRequest("创建优惠券-001")
            .with_variables(**{})
            .post("/vendor/vendorCoupon/createCouponType")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "couponTypeName":"测试优惠券1",
                    "couponTypeDesc":"",
                    "couponType":"1",
                    "receivableStartTime":"2021-04-14 00:00:00",
                    "receivableEndTime":"2021-04-30 00:00:00",
                    "faceValueStr":"1",
                    "couponLimitAmountStr":"",
                    "usableStartTime":"2021-04-14 00:00:00",
                    "usableEndTime":"2021-04-30 00:00:00",
                    "icon":"",
                    "remark":"",
                    "enable":'true',
                    "stackable":'false',
                    "canSend":'false',
                    "couponLimitType":"ALL",
                    "couponChannelType":"WECHAT",
                    "discountType":"DISCOUNT",
                    "getTpye":"NORMAL",
                    "couponTypeEnum":"NORMAL",
                    "couponUseType":"PRODUCT_QUANTITY",
                    "categories":[],
                    "includeProducts":[],
                    "totalQuantity":"1",
                    "productQuantity":"1",
                    "memberId":"$sellerId",
                    "userId":"$sellerId",
                    "vendorId":"$vendorId",
                    "depotCode":"$vendorCode",
                    "vendorCode":"$vendorCode"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()