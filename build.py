"""Generate all supported languages and device-language entry pages for GitHub Pages."""
import html,json,pathlib
root=pathlib.Path(__file__).parent
content=json.loads((root/'content.json').read_text())
base='/cooing-support/'
names={'en':'English','ko':'한국어','ja':'日本語','vi':'Tiếng Việt'}
ui={
'en':{'support':'Help & support','privacy':'Privacy policy','home':'Support & privacy','headline':'A quiet place for<br>the little moments.','intro':'Support and privacy information for Cooing, your baby care journal.','supportTitle':'A little help.<br>Back to your day.','supportIntro':'Getting started, purchases, photos, reminders and safe backups.','privacyTitle':'Your records.<br>Your device. Your choice.','privacyIntro':'How Cooing for iOS handles your information.','device':'Your care records stay on your device. You choose where to save and share backups.','supportCard':'Setup, purchase restoration, reminders and backups.','privacyCard':'Understand what is stored and the choices you have.','updated':'Updated November 7, 2026','operator':'Operator','host':'Website hosting privacy','language':'Language'},
'ko':{'support':'도움말 및 문의','privacy':'개인정보처리방침','home':'지원과 개인정보','headline':'아이의 하루를,<br>차분히 담다.','intro':'아기 돌봄 기록 앱, 쿠잉의 지원 및 개인정보 안내입니다.','supportTitle':'다시 기록에<br>집중할 수 있도록.','supportIntro':'시작·결제·사진·알림·안전한 백업에 대한 도움말입니다.','privacyTitle':'기록은 기기에.<br>선택은 사용자에게.','privacyIntro':'쿠잉 iOS 앱의 개인정보 처리 안내입니다.','device':'기록은 기기에 저장됩니다. 백업과 공유는 직접 선택한 파일로 진행합니다.','supportCard':'시작하기, 구매 복원, 알림과 안전한 백업.','privacyCard':'어디에 저장하고, 무엇을 선택할 수 있는지.','updated':'최종 수정: 2026년 11월 7일','operator':'운영자','host':'웹사이트 호스팅 개인정보 안내','language':'언어'},
'ja':{'support':'ヘルプ・お問い合わせ','privacy':'プライバシーポリシー','home':'サポートとプライバシー','headline':'小さな日々を、<br>やさしく記録。','intro':'育児記録アプリCooingのサポートとプライバシー情報です。','supportTitle':'ひとつ解決。<br>いつもの毎日へ。','supportIntro':'はじめ方、購入の復元、写真、通知、安全なバックアップのご案内です。','privacyTitle':'あなたの記録。<br>あなたの端末と選択。','privacyIntro':'Cooing iOSアプリにおける情報の取り扱いについて。','device':'育児の記録は端末内に保存されます。バックアップの保存先と共有相手は自分で選べます。','supportCard':'初期設定、購入の復元、通知とバックアップ。','privacyCard':'保存される情報と、選べることについて。','updated':'最終更新日：2026年11月7日','operator':'運営者','host':'ホスティングのプライバシー情報','language':'言語'},
'vi':{'support':'Trợ giúp và hỗ trợ','privacy':'Chính sách quyền riêng tư','home':'Hỗ trợ và quyền riêng tư','headline':'Ghi lại những ngày nhỏ,<br>thật nhẹ nhàng.','intro':'Thông tin hỗ trợ và quyền riêng tư của Cooing, ứng dụng nhật ký chăm sóc bé.','supportTitle':'Một chút trợ giúp.<br>Tiếp tục ngày của bạn.','supportIntro':'Bắt đầu sử dụng, mua hàng, ảnh, nhắc nhở và sao lưu an toàn.','privacyTitle':'Hồ sơ của bạn.<br>Thiết bị và lựa chọn của bạn.','privacyIntro':'Cách Cooing trên iOS xử lý thông tin của bạn.','device':'Nhật ký chăm sóc được lưu trên thiết bị. Bạn tự chọn nơi sao lưu và người nhận.','supportCard':'Thiết lập, khôi phục giao dịch, nhắc nhở và sao lưu.','privacyCard':'Hiểu dữ liệu được lưu và các lựa chọn của bạn.','updated':'Cập nhật ngày 7 tháng 11 năm 2026','operator':'Đơn vị vận hành','host':'Quyền riêng tư của dịch vụ lưu trữ web','language':'Ngôn ngữ'}
}
def link(lang,route=''):return base+lang+'/'+(route+'/' if route else '')
def render(lang,route,neutral=False):
 t=ui[lang];title=t[route] if route else t['home'];langdata='' if neutral else f' data-language="{lang}"'
 alternatives=''.join(f'<link rel="alternate" hreflang="{code}" href="https://m9339191.github.io{link(code,route)}">' for code in names)
 choices=''.join(f'<a href="{link(code,route)}" lang="{code}" hreflang="{code}"'+(' aria-current="page"' if code==lang and not neutral else '')+f'>{name}</a>' for code,name in names.items())
 if route:
  heading=t[route+'Title'];intro=t[route+'Intro']
  body=''.join(f'<section><h2>{html.escape(h)}</h2><p>{html.escape(p)}</p></section>' for h,p in content[lang][route])
  body='<div class="body">'+body+'</div>'
 else:
  heading=t['headline'];intro=t['intro'];body=f'<aside>{t["device"]}</aside><div class="cards"><a class="card" href="{link(lang,"support")}"><h2>{t["support"]}</h2><p>{t["supportCard"]}</p></a><a class="card" href="{link(lang,"privacy")}"><h2>{t["privacy"]}</h2><p>{t["privacyCard"]}</p></a></div>'
 return f'''<!doctype html><html lang="{lang}"{langdata} data-base="{base}" data-route="{route}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Cooing</title><meta name="description" content="{html.escape(intro,quote=True)}">{alternatives}<script src="{base}assets/language.js"></script><link rel="stylesheet" href="{base}assets/style.css"></head><body><header><a class="brand" href="{link(lang)}">Cooing</a><div class="header-right"><nav aria-label="Cooing"><a href="{link(lang,'support')}">{t['support']}</a><a href="{link(lang,'privacy')}">{t['privacy']}</a></nav><nav class="language-picker" aria-label="{t['language']}">{choices}</nav></div></header><main><div class="eyebrow">Cooing · {title}</div><h1>{heading}</h1><p class="intro">{intro}</p>{body}</main><footer><p>Cooing: Baby Care Journal</p><p>{t['operator']}: DEOK JOO MOON · <a href="mailto:it@bebriz.com">it@bebriz.com</a></p><p>{t['updated']}</p><a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement">{t['host']}</a></footer></body></html>'''
for lang in names:
 assert len(content[lang]['privacy'])==6 and len(content[lang]['support'])==6
 for route in ['','support','privacy']:
  d=root/lang/route;d.mkdir(parents=True,exist_ok=True);(d/'index.html').write_text(render(lang,route))
for route in ['','support','privacy']:
 d=root/route;d.mkdir(parents=True,exist_ok=True);(d/'index.html').write_text(render('en',route,neutral=True))
(root/'.nojekyll').touch()
print('Built 12 translated pages and 3 device-language entry pages')
