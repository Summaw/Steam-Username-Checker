import requests
import time
import random
import threading
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

def generate_creationid():
    timestamp = int(time.time() * 1000)
    random_part = random.randint(1000000, 9999999) 
    return str(timestamp) + str(random_part)

def check_username_availability(username, creationid=None):
    if creationid is None:
        creationid = generate_creationid()
    
    headers = {
        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://store.steampowered.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 AVG/139.0.0.0',
        'X-Prototype-Version': '1.7',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'accountname': username,
        'count': '1',
        'creationid': creationid,
    }

    try:
        response = requests.post('https://store.steampowered.com/join/checkavail/', headers=headers, data=data, timeout=5)
        return username, response.text, response.status_code
    except Exception as e:
        return username, f"Error: {str(e)}", 0

def setup_directories():
    if not os.path.exists('data'):
        os.makedirs('data')
    
    if not os.path.exists('Output'):
        os.makedirs('Output')

    check_file = 'data/check.txt'
    if not os.path.exists(check_file):
        with open(check_file, 'w') as f:
            f.write("DimeBaggg\nCoolGamer123\nEpicPlayer456\n")
        print(" Created data/check.txt with sample usernames")
    
    available_file = 'Output/available.txt'
    taken_file = 'Output/taken.txt'
    
    if not os.path.exists(available_file):
        with open(available_file, 'w') as f:
            pass 
    
    if not os.path.exists(taken_file):
        with open(taken_file, 'w') as f:
            pass  

def read_usernames_from_check():
    check_file = 'data/check.txt'
    try:
        with open(check_file, 'r') as f:
            usernames = [line.strip() for line in f.readlines() if line.strip()]
        return usernames
    except FileNotFoundError:
        print("❌ data/check.txt not found!")
        return []

def write_username_to_output(username, is_available, response_text):
    if is_available:
        output_file = 'Output/available.txt'
    else:
        output_file = 'Output/taken.txt'
    
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(f"{username}\n")

def remove_checked_username(username):
    check_file = 'data/check.txt'
    try:
        with open(check_file, 'r') as f:
            lines = f.readlines()
        
        lines = [line for line in lines if line.strip() != username]
        
        with open(check_file, 'w') as f:
            f.writelines(lines)
            
    except Exception as e:
        print(f"❌ Error removing {username} from check.txt: {e}")

def check_username_and_save(username):
    print(f"🔍 Checking: {username}")
    
    username_result, response_text, status_code = check_username_availability(username)
    
    is_available = "not available" not in response_text.lower() and status_code == 200
    
    write_username_to_output(username, is_available, response_text)
    
    remove_checked_username(username)
    
    if is_available:
        print(f"✅ {username} - AVAILABLE")
    else:
        print(f"❌ {username} - TAKEN")
    
    return username, is_available, response_text

def process_all_usernames():
    print("🚀 Steam Username Checker - Processing check.txt")
    print("=" * 60)
    
    while True:
        try:
            thread_count = input("How many threads do you want to use? (1-250, recommended: 5-10): ")
            thread_count = int(thread_count)
            if 1 <= thread_count <= 250:
                break
            else:
                print("Please enter a number between 1 and 250.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"🔄 Using {thread_count} threads for processing...")
    print("=" * 60)
    
    setup_directories()
    
    usernames = read_usernames_from_check()
    
    if not usernames:
        print("❌ No usernames found in data/check.txt")
        return
    
    print(f"📋 Found {len(usernames)} usernames to check")
    print("=" * 60)
    
    start_time = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_to_username = {
            executor.submit(check_username_and_save, username): username 
            for username in usernames
        }
        
        for i, future in enumerate(as_completed(future_to_username), 1):
            username, is_available, response_text = future.result()
            results.append((username, is_available, response_text))
            
            print(f"\n[{i}/{len(usernames)}] ✅ {username} - {'AVAILABLE' if is_available else 'TAKEN'}")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    available_count = sum(1 for _, is_avail, _ in results if is_avail)
    taken_count = len(results) - available_count
    
    print("\n" + "=" * 60)
    print(f"⚡ Completed {len(results)} checks in {total_time:.2f} seconds!")
    print(f"✅ Available: {available_count}")
    print(f"❌ Taken: {taken_count}")
    print(f"📁 Results saved to Output/available.txt and Output/taken.txt")
    print(f"🗑️  Checked usernames removed from data/check.txt")

if __name__ == "__main__":
    process_all_usernames()
