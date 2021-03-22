# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/22 10:53'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("我的拼团列表")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_online)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("我的拼团列表-全部-001")
            .with_variables(**{})
            .post("/spellGroup/findSpellGroupPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "groupState":"ALL",
                    "memberId":"${ENV(memberId)}",
                    "searchPageVo":{"pageIndex":1,"pageSize":10}
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("我的拼团列表-拼团中-002")
            .with_variables(**{})
            .post("/spellGroup/findSpellGroupPage")
            .with_headers(
            **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "groupState":"GROUP_ING",
                    "memberId":"${ENV(memberId)}",
                    "searchPageVo":{"pageIndex":1,"pageSize":10}
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("我的拼团列表-拼团成功-003")
            .with_variables(**{})
            .post("/spellGroup/findSpellGroupPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "groupState":"GROUP_SUCCESS",
                    "memberId":"${ENV(memberId)}",
                    "searchPageVo":{"pageIndex":1,"pageSize":10}
                }
            )
                .validate()
                .assert_equal("status_code",200)
                .assert_equal("body.msg","success")
        ),
        Step(
            RunRequest("我的拼团列表-拼团失败-004")
            .with_variables(**{})
            .post("/spellGroup/findSpellGroupPage")
            .with_headers(
                **{
                    "User-Agent":"HttpRunner/${get_httprunner_version()}",
                    "Content-Type":"application/json",
                }
            )
            .with_params(
                **{
                    "os":"min",
                    "memberId":"${ENV(memberId)}",
                    "lat":"29.71797999388022",
                    "lon":"106.63042999999999",
                    "userToken":"c857660825954391ab036eed074861ad",
                    "vendorCode":"${ENV(vendorCode)}"
                }
            )
            .with_json(
                {
                    "groupState":"GROUP_FAIL",
                    "memberId":"${ENV(memberId)}",
                    "searchPageVo":{"pageIndex":1,"pageSize":10}
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()