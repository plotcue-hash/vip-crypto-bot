from pyrogram import Client, filters

app = Client(
    "vip_crypto_bot",
    api_id=24574365,
    api_hash="519c84fdaa8c9b00043d612e98a6ff22",
    bot_token="8489549446:AAFp4Pu-ZYVWIgHkua4lhkXWKDl6gsB1O10"  # 🔹 Replace this with your real BotFather token
)

VIP_LINK = "https://t.me/+DWZL_Nd-sYEyZjg8"  # Replace with your real VIP channel link
ADMIN_ID = 5752825610  # Your Telegram ID

@app.on_message(filters.command("buy"))
async def buy_crypto(client, message):
    await message.reply_text(
        "💸 To buy VIP access with crypto:\n\n"
        "1️⃣ Send $10 worth of USDT (TRC20) to this address:\n"
        "`TGhT7vExampleWalletAddress`\n\n"
        "2️⃣ After sending, type:\n"
        "`/paid <txhash>`\n\n"
        "We'll verify and send your VIP link instantly."
    )

@app.on_message(filters.command("paid"))
async def paid_crypto(client, message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❗ Please include your TX hash. Example:\n`/paid abcd1234txhash`")
        return
    
    tx_hash = parts[1]
    await client.send_message(
        ADMIN_ID,
        f"🧾 Payment proof from {message.from_user.mention}:\nTX Hash: `{tx_hash}`"
    )
    await message.reply_text("✅ Thanks! Your payment is being verified.")

@app.on_message(filters.user(ADMIN_ID) & filters.command("approve"))
async def approve_payment(client, message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("Usage: /approve <user_id>")
        return
    
    user_id = int(parts[1])
    await client.send_message(
        user_id,
        f"🎉 Payment confirmed!\nHere’s your VIP link:\n{VIP_LINK}"
    )
    await message.reply_text("✅ Access granted to user!")

app.run()
