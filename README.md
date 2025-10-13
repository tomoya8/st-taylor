# Visualization of Taylor Series Expansion

This is a Streamlit application that visualizes the approximation of functions using Taylor series expansion.

# テイラー展開の可視化

テイラー展開による関数の近似を可視化するためのStreamlitアプリケーションです。

# Setup for Reverse Proxy

Enable the necessary Apache modules for reverse proxying:
```bash
# sudo a2enmod proxy
# sudo a2enmod proxy_http
```

Add the following configuration to your Apache virtual host file:
[Reddit Reference](https://www.reddit.com/r/StreamlitOfficial/comments/1ixw4lc/white_page_streamlit_behind_reverse_proxy/)
```
<VirtualHost *:443>
...
    ProxyPreserveHost On

    ProxyPass /st-taylor http://localhost:8501 upgrade=websocket
    ProxyPassReverse /st-taylor http://localhost:8501
</VirtualHost>
```

Then enable the site and restart Apache:
```bash
# sudo a2ensite local-ssl
# sudo systemctl restart apache2
```

To run this application behind a reverse proxy,
it is recommended to set the `STREAMLIT_SERVER_ENABLE_CORS` environment variable to `false`.

```bash
export STREAMLIT_SERVER_ENABLE_CORS=false
streamlit run app.py
```

