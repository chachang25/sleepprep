# Sleep Prep Hub - Static Deployment

This is a pre-built version of the Sleep Prep Hub app optimized for Vercel deployment.

## Deploy to Vercel

### Option 1: Deploy this folder directly

1. Copy the `static-deploy` folder to a new repository:
   ```bash
   mkdir sleep-prep-hub && cp -r static-deploy/* sleep-prep-hub/
   cd sleep-prep-hub
   git init && git add . && git commit -m "Sleep Prep Hub"
   ```

2. Push to GitHub:
   ```bash
   gh repo create sleep-prep-hub --public --source=. --push
   # OR
   git remote add origin https://github.com/YOUR_USERNAME/sleep-prep-hub.git
   git push -u origin main
   ```

3. Deploy on Vercel:
   - Go to [vercel.com](https://vercel.com)
   - Import the repository
   - **No build settings needed** - just click Deploy!

### Vercel Settings

| Setting | Value |
|---------|-------|
| Framework Preset | Other |
| Build Command | (leave empty) |
| Output Directory | `.` |
| Install Command | (leave empty) |

## Files

```
static-deploy/
├── index.html          # Complete app (HTML + CSS + JS)
├── vercel.json         # Vercel routing config
└── api/                # Python serverless functions
    ├── index.py        # GET /api/ health check
    ├── journal-prompt.py   # Daily prompt
    └── journal-prompts.py  # All prompts
```

## Features

- Programmable bedtime timer (default 9 PM)
- Tonight's override for schedule deviations
- Box breathing exercise (4-4-4-4 pattern)
- Evening journal with daily prompts
- Tomorrow's Big 3 priorities
- Worry dump with 2-minute timer
- Gratitude anchor
- Browser push notifications
- Dark mode theme
- All settings saved to localStorage
