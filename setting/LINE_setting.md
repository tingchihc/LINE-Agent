![Alt text](https://github.com/tingchihc/LINE-Agent/blob/3509ed4ffd1fc32c3cfa093f59fcc15688845e97/images/access%20token.png)
![Alt text](https://github.com/tingchihc/LINE-Agent/blob/3509ed4ffd1fc32c3cfa093f59fcc15688845e97/images/access%20token.png)

## 🔑 How to Get `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_CHANNEL_SECRET`

To integrate your LINE chatbot with your backend (e.g., FastAPI), you need two credentials from the [LINE Developers Console](https://developers.line.biz/console/):

---

### 📘 Step-by-Step Guide

#### 1. Create a LINE Login Provider (if you haven’t yet)

- Go to: [https://developers.line.biz/console/](https://developers.line.biz/console/)
- Click **`+ Create new provider`**
- Enter a name (e.g., `MyChatbotProvider`) and click **Create**

---

#### 2. Create a New Messaging API Channel

- Inside your provider, click **`+ Create a new channel`**
- Select **Messaging API**
- Fill in:
  - **App icon** (optional)
  - **Channel name**
  - **Channel description**
  - **Category** and **Subcategory**
  - **Email address**
- Agree to the terms and click **Create**

---

#### 3. Get Your Credentials

- Open the newly created channel
- Go to the **Basic settings** tab  
  🔐 **Channel secret**: Click **Show** to reveal your `LINE_CHANNEL_SECRET`
- Go to the **Messaging API** tab  
  🔑 **Channel access token**: Click **Issue** to generate your `LINE_CHANNEL_ACCESS_TOKEN`  
  _(You can reissue or revoke it anytime)_

---

#### 4. Set Webhook URL (for FastAPI or any backend)

- In the **Messaging API** tab:
  - Scroll down to **Webhook settings**
  - Turn **Use webhook** ON
  - Set your **Webhook URL** (e.g., from [ngrok](https://ngrok.com/): `https://xxxxx.ngrok-free.app/webhook`)
  - Click **Verify**

---

#### 5. Save to Environment Variables

Create a `.env` file in your root directory:

```env
LINE_CHANNEL_SECRET=your_channel_secret
LINE_CHANNEL_ACCESS_TOKEN=your_channel_access_token
