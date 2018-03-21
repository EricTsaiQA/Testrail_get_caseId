from testrail import *

client = APIClient('https://nook.testrail.com/')
client.user = "your_account"
client.password = "your_password"


def get_automation_case():
    # 利用project id, test suite id 去取得一個test suite的裡面的test cases
    # Android - Functional   , project id 是 28
    # Quicklooks , test suite id 是 579
    project_id = input("please input project id :")
    suite_id = input("please input test suite id :")
    cases_in_suite = client.send_get('get_cases/%s&suite_id=%s' % (project_id, suite_id))
    cases_id_type_automation = []

    # 利用for迴圈去找出 test case 其 type 為automation 的 case, 並加入到一個list 此list即可當作創建 test run時使用
    for i in range(len(cases_in_suite)):
        # 7 即代表 type 為 automation
        if 7 in cases_in_suite[i].values():
            cases_id_type_automation.append(cases_in_suite[i].get('id'))


if __name__ == "__main__":
    get_automation_case()
