# -*- coding:utf-8 -*-

from alipay import AliPay

from .import setting
# app_private_key_string = open("/path/to/your/private/key.pem").read()
# alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()

# app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
# MIIEpAIBAAKCAQEApkFnp38PSslhn4wvRarL40+WtVpan6tVT55FWzAzLfQ8PfqZE2qW7mCJy1/zM07+S5L+X0pC+F7BlT+0z4rlxraG5D23khWfHb4x+uDi0Wd94eaVB0PzQXCYYBChuORvNN5YLTspeP7rNQ2OcdpGx2KUzo9w59dVW+AweblFl7GqPkRSC0P5XbkJtwnEAd0Nc08HzJR0OWZT9HRFOA7coaude9uSwDsXmsdkSNGsGDcaGEY6aGk2Tj9Fyni9LJJcOXwGrUuGDpdcP2tYePrFUGMDml/feFR9QGUbExWh/ZNpb9lKLwOtXOhQj9slilp+YJek/rLlSgW9K1WrYpuuBwIDAQABAoIBADN1mRzKAjS2wmW84UDiDbus/cviTJyRTpWXOoZwE9dMen0AnPLakh70eJIff8pI0AMaW2upM7NmuOp2ToPSzS5FftkUlUY9NQPiw9uQUgRY0Sjj0wrtqFSAAlnxq+zrn9QwYgCWCE8wMCM6r/Vjh3bdd4u78EmCaCRI7xguFXFPB9NY9oCFiwsTFJtXPZo+DSIQjqIDnh8YtV3NzrA3Ln3DsKMAr+vnPMeljAL5US6Rt5tOQY0qa9bUi6RqQwTLADcANd49YOvlr7OLjwi5jkeJ16j1nKgpasAIg9V+rF085u+PEKkLL3WJHwmhiIxrA11bxCnm1fRdfHbyWZKY9yECgYEA0k3wS7A7rzhtpznc5ZfVGWIEQ5IahRkqVGbc6wFIXKXnypOtGKAFiRmEPwm9xRurlo8TJ1bjK4D4ljEANJhX2NnIZfK3YDdNEN6D4GnEvPFR641M8M47Z7ItvdRKre8P2/ThXhkMnq5/1y7e87xvE6/a1Tr44+hclHvQWPRrsPcCgYEAymFEy0/2xAX+si4S8pzrgLfBg3Ehjan8T6JZZNCKhR7b/IT+3/AWJimzEL6jYQMlhy7QzZbRb1ssIIzqPFcFQYjQE0n6fswJuN4+jayW9Jtjvar/zhHFjW3EODR5yEDTvS3CHqQLeG3ce+srMJSxVDJR2V9ortFeb+VPbWZ+t3ECgYEAxPYvvoNwcpuzvvGnW/RGpb4x5iL46Xz3MxMfho2t+u961jRW4oBEjvGx9OQnsmpG2vxm4Oo0WnMw3mFIIvonFDZrxGd8rQU+DTWJZ21Hz/lnUugEjmdoJacvxeEEjEAgp02CoQFu21Ls8li4gKgTk+mYVyojHjhqNLp9GELadWMCgYEAi0RSXgLCEnT5p03zdgcsPOC3ByfT6jO+0GItWCX2HNN2mRhAeIQ0CcEKW4yEy56ptZQu1jtiFlpMTH4MNse/czCd15hCC/2G9zPhIgdRvjQsd/nznLA4HTIbJH5gC8EotHeHrSRATHh1kMTtbLn2KbWTA54XYK3tad0IQoWUz9ECgYBBc+kCJsb0shaRIRP5nmeb5tZCH7Yq9DgriwcIlK74cxW9fvL94n91Y6M8vSZ6MC7vF5wmcXMj3K1of04qizKbbKxCCYeOIHhTh0dB+ualDxu5WBG/6mLWR3HVHazqRVri9qoZ/3zNDx5CRNi81VpzOPmVtuos5d9sZZaNR3lkRQ==
# -----END RSA PRIVATE KEY-----
# """
#
# alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwU9mMZHHlQPE9FcxVtXOXhbWCtuDZLJRVCiofdbTVmRXrx47yGniPehwcKIsqhzhEaXBG2QhpIZUL8YsCav0mkrppoRvWOytuGyxNRESo8I6DWRs0aCq6P3AuiD9kSXET4dpAuRYT/+JrMXIZTycEts6vYYNAT9QivXJoa2FmiCQBAL3HP7F36pby9VstObilxXQcoBBJwEYGf2TK6moFFZ1dkloRr5Cfk/G82DpuVfrt1gr4OuIDWtcE3MZTrvDgTqtkRuwGF76FY3+8xUCUbJs1dL5cXYN7/b3jPcXVcdKXFj4WrOQd42ofE1BJWMxBW7L3Qlxue1vy+NGx/CuKwIDAQAB
# -----END PUBLIC KEY-----
# """

alipay = AliPay(
    appid=setting.APPID,
    app_notify_url=None,  # the default notify path
    app_private_key_string=setting.APP_PRIVATE_KEY_STRING,
    # alipay public key, do not use your own public key!
    alipay_public_key_string=setting.ALIPAY_PUBLIC_KEY_STRING,
    sign_type=setting.SIGN_TYPE, # RSA or RSA2
    debug=setting.DEBUG  # False by default
)

gateway = setting.GATEWAY
# alipay_url='https://openapi.alipaydev.com/gateway.do?'
# order_string = alipay.api_alipay_trade_page_pay    (
#     out_trade_no="20161112www4334",
#     total_amount=9999,
#     subject='韩红版充气娃娃',
#     return_url="https://www.luffycity.com/free-course",
#     notify_url="https://www.luffycity.com/free-course"
# )
# print(gateway+order_string)
























