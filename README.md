# 🎥 Telegram YouTube Downloader Bot

Un bot Telegram qui permet de télécharger et d'envoyer des **vidéos** ou des **audios** depuis YouTube directement dans la conversation. Le fichier est supprimé automatiquement du serveur après envoi.

## ✨ Fonctionnalités

- ✅ Téléchargement de vidéos YouTube en différentes qualités (360p, 720p, 1080p…)
- ✅ Téléchargement de pistes audio uniquement (m4a)
- ✅ Envoi direct du fichier dans Telegram (en tant que `video` ou `audio`)
- ✅ Nettoyage automatique du fichier après envoi
- ✅ Interface avec boutons Telegram (qualité, audio/vidéo)
- ✅ Support des noms de fichiers avec espaces et caractères spéciaux

## 📦 Dépendances

- Python 3.10+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (v20+)
- [pytubefix](https://pytubefix.readthedocs.io/)
- `asyncio`

### Installation

```bash
git clone https://github.com/enocben/TeleTubeBot.git
cd TeleTubeBot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
