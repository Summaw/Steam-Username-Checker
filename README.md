# Steam Username Checker 🚀

A fast, multi-threaded tool to check Steam username availability in bulk. Check hundreds of usernames simultaneously to find available ones for your Steam account.

## ✨ Features

- **Lightning Fast**: Multi-threaded processing with configurable thread count (1-250)
- **Bulk Processing**: Check hundreds of usernames from a text file
- **Smart Organization**: Automatically sorts results into available and taken usernames
- **Dynamic CreationID**: Generates unique Steam creation IDs to avoid rate limiting
- **Real-time Progress**: See results as they come in
- **Clean Output**: Simple text files with just usernames, no clutter

## �� Quick Start

1. **Install Requirements**
   ```bash
   pip install requests
   ```

2. **Prepare Your Usernames**
   - Create a `data/check.txt` file
   - Add one username per line:
     ```
     CoolGamer123
     EpicPlayer456
     NinjaWarrior
     ```

3. **Run the Checker**
   ```bash
   python main.py
   ```

4. **Choose Thread Count**
   - Enter your preferred thread count (1-250)
   - Recommended: 5-10 threads for stable performance
   - Higher threads = faster but more aggressive

## 📁 File Structure

```
steam-username-checker/
├── main.py              # Main script
├── data/
│   └── check.txt       # Input usernames (one per line)
└── Output/
    ├── available.txt    # Available usernames
    └── taken.txt       # Taken usernames
```

## 🔧 How It Works

1. **Reads** usernames from `data/check.txt`
2. **Generates** unique Steam creation IDs for each request
3. **Checks** availability via Steam's API endpoint
4. **Organizes** results into appropriate output files
5. **Removes** checked usernames from the input file
6. **Shows** real-time progress and statistics

##  Output Format

### Available Usernames (`Output/available.txt`)
```
CoolGamer123
EpicPlayer456
NinjaWarrior
```

### Taken Usernames (`Output/taken.txt`)
```
TakenUsername1
TakenUsername2
```

## ⚡ Performance

- **Single Thread**: ~1 username/second
- **10 Threads**: ~8-10 usernames/second
- **50 Threads**: ~30-40 usernames/second
- **100+ Threads**: ~60+ usernames/second

*Performance may vary based on internet speed and Steam's server response times*

## 🛡️ Rate Limiting & Safety

- **Respectful**: Built-in delays and unique creation IDs
- **Configurable**: Choose thread count based on your needs
- **Steam-Friendly**: Uses official Steam endpoints
- **Error Handling**: Gracefully handles network issues

## 🔍 Steam API Details

- **Endpoint**: `https://store.steampowered.com/join/checkavail/`
- **Method**: POST request with form data
- **Headers**: Mimics real browser requests
- **CreationID**: Dynamic timestamp-based identifier

## 📝 Usage Examples

### Check a Few Usernames
```bash
# Add usernames to data/check.txt
echo "MyUsername123" >> data/check.txt
echo "CoolGamer456" >> data/check.txt

# Run with 5 threads
python main.py
# Enter: 5
```

### Bulk Check Hundreds
```bash
# Generate random usernames (optional)
# Add to data/check.txt

# Run with 20 threads for speed
python main.py
# Enter: 20
```

## ⚠️ Important Notes

- **Steam Terms**: Use responsibly and respect Steam's terms of service
- **Rate Limiting**: Higher thread counts may trigger Steam's anti-bot measures
- **Network**: Requires stable internet connection
- **Legal**: Only check usernames you have permission to check

## 🐛 Troubleshooting

### Common Issues

1. **"No usernames found"**
   - Ensure `data/check.txt` exists and contains usernames
   - Check file permissions

2. **Connection errors**
   - Verify internet connection
   - Try reducing thread count
   - Check if Steam is accessible

3. **Slow performance**
   - Increase thread count (within reason)
   - Check internet speed
   - Steam servers may be slow

### Error Messages

- **FileNotFoundError**: Missing `data/check.txt`
- **ConnectionTimeout**: Network or Steam server issues
- **ValueError**: Invalid thread count input

## 🔄 Updates & Maintenance

- **Auto-cleanup**: Checked usernames are automatically removed
- **Fresh creation IDs**: Generated for each request
- **Session management**: No persistent sessions to maintain

## 📈 Future Enhancements

- [ ] Proxy support for IP rotation
- [ ] Username generation algorithms
- [ ] Export to CSV/JSON formats
- [ ] GUI interface
- [ ] Scheduled checking
- [ ] Discord/Telegram notifications

## 📄 License

This project is for educational and personal use. Please respect Steam's terms of service and use responsibly.

---

**Happy username hunting! **

*Remember: With great power comes great responsibility. Use this tool ethically and don't abuse Steam's services.*
