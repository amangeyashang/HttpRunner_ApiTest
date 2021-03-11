# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/5 15:31'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("拼团订单列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("拼团订单列表-全部-001")
                .with_variables(**{})
                .post("/spellGroup/findSpellGroupOrderList")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "groupState":"ALL",
                    "memberId":2494,
                    "searchPageVo":
                        {
                            "pageIndex":1,
                            "pageSize":10
                        }
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("拼团订单列表-拼团中-002")
                .with_variables(**{})
                .post("/spellGroup/findSpellGroupOrderList")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "groupState":"GROUP_ING",
                    "memberId":2494,
                    "searchPageVo":
                        {
                            "pageIndex":1,
                            "pageSize":10
                        }
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("拼团订单列表-拼团成功-003")
                .with_variables(**{})
                .post("/spellGroup/findSpellGroupOrderList")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "groupState":"GROUP_SUCCESS",
                    "memberId":2494,
                    "searchPageVo":
                        {
                            "pageIndex":1,
                            "pageSize":10
                        }
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("拼团订单列表-拼团失败-004")
                .with_variables(**{})
                .post("/spellGroup/findSpellGroupOrderList")
                .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
                .with_json(
                {
                    "groupState":"GROUP_FAIL",
                    "memberId":2494,
                    "searchPageVo":
                        {
                            "pageIndex":1,
                            "pageSize":10
                        }
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        )
    ]