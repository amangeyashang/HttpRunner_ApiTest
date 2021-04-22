# -*- coding:utf-8 -*-
_author_ = 'Leo'
__date__ = '2021/3/17 14:38'

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
class TestCaseDemoTestcaseRequest(HttpRunner):

    config = (
        Config("更新头像")
            .variables(**{})
            .base_url("${ENV(base_url_wechat_develop_rest)}")
            .verify(False)
            .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("更新头像-001")
            .with_variables(**{})
            .post("/users/updateimage")
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
                    "lat":28.45362,
                    "lon":109.006128,
                    "userToken":"684f2aa256a6408980cbb1f56602e250",
                }
            )
            .with_json(
                {
                    "image":"https://thirdwx.qlogo.cn/mmopen/vi_32/Fe69ooH7h6cpbtjjADkLnZ4weFBpP4iaL0wZEcIReeyQZicmzn2HBGAkk4kQvwaITdc8sKBIjybpZbfg9NRqa2OA/132"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","success")
        )
    ]

if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()