#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import json
import os
import time

import requests


def check_cloud(name, local_ver=1.0):
    res = requests.get("https://jihulab.com/vhook/control/-/raw/main/ver.json")

    if res.status_code == 200:
        try:
            json.loads(res.text)
        except json.JSONDecodeError:
            return
        verRes = res.json().get(name, {})
        if verRes:
            print(f"{'*' * 20}公告{'*' * 20}")
            r_ver = verRes['ver']
            r_log = verRes['log']
            r_tip = verRes['tip']
            r_open = verRes['open']
            r_date = verRes['date']
            r_tg = verRes['tg']
            r_inviteUrl = verRes['inviteUrl']
            if not r_open:
                content = f"【提示】：{r_tip}"
                content += f"\n【反馈】：{r_tg}"
                content += f"\n{'*' * 20}公告{'*' * 20}"
                print(content)
                exit()
            if local_ver < r_ver:
                content = "*【提示】：🔔🔔🔔发现新版本，避免封号，请更新至最新版本！！！"
                content += f"\n*【版本】：本地（V{local_ver}） 云端（V{r_ver}）"
                content += f"\n*【日期】：{r_date}"
                content += f"\n*【日志】：{r_log}"
                content += f"\n*【反馈】：{r_tg}"
                if r_inviteUrl:
                    content += f"\n*【入口】：{r_inviteUrl}"
                content += f"\n{'*' * 20}公告{'*' * 20}"
                print(content)
                exit()
            content = f"【版本】：V{local_ver}"
            content += f"\n【反馈】：{r_tg}"
            if r_inviteUrl:
                content += f"\n【入口】：{r_inviteUrl}"
            content += f"\n{'*' * 20}公告{'*' * 20}"
            print(content)


def getEnv(key, tips, ver=1.0):
    check_cloud(key, ver)
    time.sleep(1)
    env_str = os.getenv(key)
    if env_str:
        try:
            env_str = json.loads(
                env_str.replace("'", '"').replace("\n", "").replace(" ", "").replace("\t", ""))
            print(f"\n----------共获取到{len(env_str)}个账号----------\n")
            return env_str  # line:350
        except Exception as e:  # line:351
            print(f'请检查变量[{key}]参数是否填写正确{e}')
    else:
        print(f'# 未找到青龙变量【{key}】，请按照下方格式配置\nexport {key}{tips}')
        exit()
