import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
p = 0
def get_page_data(page):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cookie': '_yep_uuid=922d163b-55c7-dc3d-59d0-68783b18703a; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank_04%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank_04%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1716877636_1392598982; fu=573932232; _gid=GA1.2.2063335793.1716877639; Hm_lvt_f00f67093ce2f38f215010b699629083=1716877639; supportwebp=true; supportWebp=true; _csrfToken=c1709528-0ed0-40b5-af89-2a74a7f87dee; _yep_uuid=e920c0aa-c803-136f-ec3a-efdb15fcea22; traffic_utm_referer=https%3A//www.google.com/; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D; x-waf-captcha-referer=; _gat_gtag_UA_199934072_2=1; _ga=GA1.1.1236408422.1716877639; _ga_FZMMH98S83=GS1.1.1716895383.4.0.1716895383.0.0.0; _ga_PFYW0QLV3P=GS1.1.1716895383.4.0.1716895383.0.0.0; Hm_lpvt_f00f67093ce2f38f215010b699629083=1716895384; w_tsfp=ltvgWVEE2utBvS0Q6Kzhk0yoFT47Z2R7xFw0D+M9Os09BqsoV52N1oF/ttfldCyCt5Mxutrd9MVxYnGHXt8geRARQMmWb5tH1VPHx8NlntdKRQJtA5zcWwEZcLMmv2ZGemsPIBG13Tl8LdQQmbJpjQxd5SR037ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgX2NuwDuLi02VukdjVCQo3xOSi1nqFHud/xfQw6xMZ/9BrJy8GKv0DPlapCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZViygr4ke665KvR24WRKB+8KFEsfu1katec6qBZKCiq5ZiOOA/t/vFYCR/da+5yqcCnGgsi5MkU=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    response = requests.get('https://www.qidian.com/rank/recom/datetype3//page{}/'.format(page), headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank_view_list = soup.find("div", id="rank-view-list").find_all("h2")
    cur_df = pd.DataFrame(columns=["name", "author", "type", "status", "month_ticket", "week_ticket", "reward_num", "description", "update_time", "count_words", "recommend_num"])
    for each in rank_view_list[0:5]:
        book_link = "https:" + each.a["href"]
        book_detail = get_book_detail(book_link)
        cur_df = cur_df._append(book_detail, ignore_index=True)
        # 進度條
        global p
        p+=1
        sys.stdout.write('\r')
        sys.stdout.write('downloading : '+'['+'='*p+' '*(25-p)+']')
        sys.stdout.flush()
    return cur_df
    

def get_book_detail(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cookie': '_yep_uuid=922d163b-55c7-dc3d-59d0-68783b18703a; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank_04%22%2C%22eid%22%3A%22%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l1%22%3A5%2C%22pid%22%3A%22qd_P_rank_04%22%2C%22eid%22%3A%22%22%7D; newstatisticUUID=1716877636_1392598982; fu=573932232; _gid=GA1.2.2063335793.1716877639; Hm_lvt_f00f67093ce2f38f215010b699629083=1716877639; supportwebp=true; supportWebp=true; _csrfToken=c1709528-0ed0-40b5-af89-2a74a7f87dee; _yep_uuid=e920c0aa-c803-136f-ec3a-efdb15fcea22; traffic_utm_referer=https%3A//www.google.com/; e2=; e1=%7B%22l6%22%3A%22%22%2C%22l1%22%3A3%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D; x-waf-captcha-referer=; _gat_gtag_UA_199934072_2=1; _ga=GA1.1.1236408422.1716877639; _ga_FZMMH98S83=GS1.1.1716895383.4.0.1716895383.0.0.0; _ga_PFYW0QLV3P=GS1.1.1716895383.4.0.1716895383.0.0.0; Hm_lpvt_f00f67093ce2f38f215010b699629083=1716895384; w_tsfp=ltvgWVEE2utBvS0Q6Kzhk0yoFT47Z2R7xFw0D+M9Os09BqsoV52N1oF/ttfldCyCt5Mxutrd9MVxYnGHXt8geRARQMmWb5tH1VPHx8NlntdKRQJtA5zcWwEZcLMmv2ZGemsPIBG13Tl8LdQQmbJpjQxd5SR037ZlCa8hbMFbixsAqOPFm/97DxvSliPXAHGHM3wLc+6C6rgv8LlSgX2NuwDuLi02VukdjVCQo3xOSi1nqFHud/xfQw6xMZ/9BrJy8GKv0DPlapCs2RYj4VA3sB49AtX02TXKL3ZEIAtrZViygr4ke665KvR24WRKB+8KFEsfu1katec6qBZKCiq5ZiOOA/t/vFYCR/da+5yqcCnGgsi5MkU=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'referer': 'https://www.qidian.com/rank/recom/datetype3/',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = {}
    result["name"] = soup.find("h1", id="bookName").text.strip()
    result["author"] = soup.find("span", class_="author").text.strip().split(":")[-1]
    result["update_time"] = soup.find("span", class_="update-time").text.strip().split(":", 1)[-1]
    dd = soup.find("p", class_="book-attribute")
    result["type"] = dd.find("a", rel="nofollow").text.strip()
    result["status"] = dd.find("span").text.strip()
    dd = soup.find("p", class_="count")
    dd2 = dd.find_all("em")
    result["count_words"] = dd2[0].text.strip()[:-1]
    result["recommend_num"] = dd2[1].text.strip()[:-1]
    result["description"] = soup.find("p", id="book-intro-detail").text.strip()
    result["month_ticket"] = soup.find("p", id="monthCount").text.strip()
    result["week_ticket"] = soup.find("p", id="recCount").text.strip()
    result["reward_num"] = soup.find("span", id="rewardNum").text.strip()
    return result

def main():
    df = pd.DataFrame(columns=["name", "author", "type", "status", "month_ticket", "week_ticket", "reward_num", "description", "update_time", "count_words", "recommend_num"])
    for i in range(1, 6):
        df = pd.concat([df, get_page_data(i)], ignore_index=True)

    df.to_csv("qidian.csv", index=False)

if __name__ == "__main__":
    main()