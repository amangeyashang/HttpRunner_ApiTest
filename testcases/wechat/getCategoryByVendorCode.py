# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 14:44'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("店铺分类信息")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("店铺分类信息-001")
                .with_variables(**{})
                .get("/product/getCategoryByVendorCode")
                .with_params(
                    **{
                        "os":"min",
                        "memberId":"2494",
                        "lat":"29.71797999388022",
                        "lon":"106.63042999999999",
                        "userToken":"a07a113e2bc043058e10d36382a816a4",
                        "vendorCode":"VC10003"
                    }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]
