FROM n8nio/n8n:1.5.1

ENV N8N_HOST=0.0.0.0 \
    N8N_PORT=5678 \
    WEBHOOK_URL=https://zeroquant-live.onrender.com/webhook

EXPOSE 5678

CMD ["n8n"]
CMD ["tini", "--", "n8n"]
