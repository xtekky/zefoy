import requests
import time

# អាសយដ្ឋានវេបសាយដែល Bot ត្រូវទៅទាញយក Views
url = "https://zefoy.com/" 

# ព័ត៌មាន Headers ដើម្បីបន្លំថាជា Browser មនុស្សប្រើ
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "origin": "https://zefoy.com",
    "referer": "https://zefoy.com/"
}

def send_views(video_url):
    # ក្នុងដំណាក់កាលនេះ កូដត្រូវដោះស្រាយ Captcha ជាមុនសិន
    # បន្ទាប់មកទើបផ្ញើ Link វីដេអូទៅកាន់ Server
    payload = {
        "url": video_url,
        "service": "views" # ឬ "likes", "shares"
    }
  
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            print("Successfully sent request!")
        else:
            print("Failed to send request.")
    except Exception as e:
        print(f"Error: {e}")

# ដាក់ Link វីដេអូ TikTok របស់អ្នកនៅទីនេះ
my_video = "https://www.tiktok.com/@user/video/123456789"
send_views(my_video)
Instead of unpatching every 2 days, I made a course to teach you guys exactly how i made zefoy bot and much much more and also 5+ years of reverse engineering knowledge:

https://whop.com/reverser-academy
<img width="782" alt="image" src="https://github.com/user-attachments/assets/c1060466-14a4-4dc3-bc8d-2e8ce19c96ad" />

unpatched
> - added manual solving + cloudflare fix    
> - unstable    
> - need to put your own sessid sometimes   
> - you can find your cloudflare cookies and sessid on zefoy.com under the cookies tab   

#### Demo (outdated)

https://user-images.githubusercontent.com/98614666/200188523-f90b752d-dbe6-443a-9a84-61961a3489a1.mp4
