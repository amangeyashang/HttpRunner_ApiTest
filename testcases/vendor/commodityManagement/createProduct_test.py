# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/15 15:06'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("发布商品")
            .variables(**{})
            .base_url("${ENV(base_url_vendor_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("发布商品-001")
            .with_variables(**{})
            .post("/newVendorProduct/createProduct.do")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_json(
                {
                    "presalePickTime":"",
                    "presaleEndTime":"",
                    "saleStatus":"ON_SALE",
                    "isLooseScale":'false',
                    "salesType":"NORMAL",
                    "baseProductId":-1,
                    "brandId":-1,
                    "breif":"",
                    "categoryId":"535296001255170048",
                    "extendVos":
                        [
                            {
                                "categoryId":"535295014801006592",
                                "extendType":"OPTION",
                                "idx":1,
                                "key":"xianxian ",
                                "label":"新鲜程度",
                                "options":
                                    [
                                        {
                                            "value":"一般",
                                            "idx":1,
                                            "isHighlightShow":'null'
                                        },
                                        {
                                            "value":"新鲜",
                                            "idx":2,
                                            "isHighlightShow":'null'
                                        },
                                        {
                                            "value":"特鲜",
                                            "idx":3,
                                            "isHighlightShow":'null'
                                        }
                                    ]
                            },
                            {
                                "categoryId":"535295014801006592",
                                "extendType":"OPTION",
                                "idx":1,
                                "key":"wei1",
                                "label":"辣",
                                "options":
                                    [
                                        {
                                            "value":"微辣",
                                            "idx":0,
                                            "isHighlightShow":'null'
                                        },
                                        {
                                            "value":"特辣",
                                            "idx":1,
                                            "isHighlightShow":'null'
                                        }
                                    ]
                            }
                        ],
                    "images":["","","","",""],
                    "introImages":["","","","","","","","",""],
                    "logo":"d28e13ad-91d7-4152-917b-b030bdafc314",
                    "name":"测试商品",
                    "seoKeywords":"",
                    "seoDescription":"",
                    "seoTitle":"",
                    "subTitle":"",
                    "deposit":"",
                    "discountRate":"",
                    "balancePaymentStart":"",
                    "balancePaymentEnd":"",
                    "type":"TYPE_A",
                    "weight":500,
                    "unit":"",
                    "marketPrice":"9",
                    "finalPrice":"8",
                    "stock":"10",
                    "categoryIdF":"535295014801006592",
                    "categoryIdS":"535295132354764800",
                    "vendorCategoryF":"198",
                    "vendorCategoryS":"199",
                    "vendorCategoryId":"200",
                    "i18nCode":"21031500000003",
                    "costPrice":"7",
                    "stockWarnValue":"1",
                    "memberId":"${ENV(memberId)}",
                    "userId":"${ENV(memberId)}",
                    "vendorId":"${ENV(vendorId)}",
                    "depotCode":"${ENV(vendorCode)}",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","创建商品失败，请检查商品条码是否重复！")
        )
    ]