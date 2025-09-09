# Cloudflare Page Rules for HTTPS Redirect

If you're using Cloudflare, you can set up page rules to force HTTPS:

## Page Rule Setup:

1. **Go to Cloudflare Dashboard** → Your domain → Page Rules

2. **Create Page Rule #1: Force HTTPS**
   - **URL Pattern**: `http://cfdhandbook.com/*`
   - **Setting**: Always Use HTTPS
   - **Status**: ON

3. **Create Page Rule #2: Force HTTPS (www)**
   - **URL Pattern**: `http://www.cfdhandbook.com/*`
   - **Setting**: Always Use HTTPS
   - **Status**: ON

4. **Create Page Rule #3: Redirect www to non-www (optional)**
   - **URL Pattern**: `https://www.cfdhandbook.com/*`
   - **Setting**: Forwarding URL (301 Redirect)
   - **Destination**: `https://cfdhandbook.com/$1`
   - **Status**: ON

## SSL/TLS Settings:

1. **Go to SSL/TLS** → Overview
2. **Set encryption mode**: Full (strict) or Full
3. **Enable**: Always Use HTTPS
4. **Enable**: HTTP Strict Transport Security (HSTS)

## Security Settings:

1. **Go to SSL/TLS** → Edge Certificates
2. **Enable**: Always Use HTTPS
3. **Enable**: HTTP Strict Transport Security (HSTS)
4. **Set HSTS Settings**:
   - Max Age Header: 6 months (15768000)
   - Include Subdomains: ON
   - Preload: ON (optional)

This will ensure all HTTP requests are automatically redirected to HTTPS.