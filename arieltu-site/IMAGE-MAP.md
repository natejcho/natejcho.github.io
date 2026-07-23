# Placeholder → real image map

Every image on the site is currently a gray labeled SVG in `/assets`.
To restore your real images, download them from your Squarespace CDN
(**before canceling Squarespace**), save each one into `/assets` with the
name in the left column (as `.jpg`/`.png`), then find-and-replace the
`.svg` extension with the real extension in the HTML files.

| Placeholder file | Page | Original Squarespace CDN URL |
| --- | --- | --- |
| arieltu-portrait | About | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/4df5c48b-8727-423c-8879-3cf5bad67820/arieltu.jpg |
| doc-chip-boom | Documentaries | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/cd859a30-df82-455a-a21e-a0a4d59c45d4/invisible+costs+of+TW+chib+boom.png |
| doc-superstitions | Documentaries | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/73a7f36c-ab92-4b31-bff2-89c70274ac13/Superstitions |
| doc-dw-ryan-righ | Documentaries | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/bf70ecce-8022-4cd4-8859-8a2e83b0f7d7/%E5%85%A9%E5%B2%B8%E7%AC%AC%E4%B8%80%E5%B0%8D%EF%BC%9ARyan%E8%88%87Righ%E7%9A%84%E5%90%8C%E5%A9%9A%E4%B9%8B%E8%B7%AF.mp4.00_00_37_04.Still001.png |
| doc-rittenhouse | Documentaries | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/42edb898-ec4e-4fbb-b0a9-881f3bf7734e/the+trials+of+kyle+rittenhouse.png |
| project-1 | Projects | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532227986266-M54DZSPHURIA3MQVP4KN/1.jpg |
| project-2 | Projects | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532229356969-8PPBPNVMBQLCVZTI9D8V/2.jpg |
| project-3 | Projects | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532229615014-WRDWQ5CC57ODFX1CD7H6/3.jpg |
| photo-rally-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/b10da4bd-9363-415d-b1b0-cb475c8ecb31/IMG6686-R01-015.jpg |
| photo-rally-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/4372f865-1b4b-45ca-9492-724b15361d14/IMG6686-R01-013.jpg |
| photo-rally-3 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/450aff4b-75e3-472f-bb69-a3662389fcfb/IMG6686-R01-033.jpg |
| photo-heatwave-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532253796706-AOHGVOHON80X2BXBRAW7/c5749a59dab24401bccf1b8e5839573e.jpg |
| photo-heatwave-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532253549275-UOYDV9434Y50DSVZO7JB/d6235f1145444fe59489fd8f6e503be3.jpg |
| photo-heatwave-3 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532253752835-PW32S37OCY797Z5MXO42/69ff201f9d324b2f80f4e3a96b1ba06d.jpg |
| photo-heatwave-4 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532253660801-HJNEMDTBPHO656O1KRU5/b9a36e6569754493bc46fd57cedc02f2.jpg |
| photo-heatwave-5 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532253831592-8KYYZB2DWPLOE9CHKQQQ/1dee99a73d6d4f168e9218d86dfae08e.jpg |
| photo-heatwave-6 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532254096462-TT1QAMG8SX0HUSSKG00E/IMG_2224+%281%29.JPG |
| photo-metoo-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532254257278-DR1FFYI495CHBVF69T2B/IMG_2354.JPG |
| photo-metoo-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532254477895-63AHFPMC3R141BVWBHQK/IMG_1988.JPG |
| photo-skidrow-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532254566930-9DE79RPRRV70VR5JB5Y8/image-asset.jpeg |
| photo-skidrow-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532254823613-VL87N6YUHTANO0M8UBHS/5acfad812000002d00eb48b0.jpeg |
| photo-skidrow-3 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255193909-PW0X39K9FYMH6YDMPZSU/header.jpg |
| photo-caregivers-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255228204-TFGK2EAW2C8XG8TDWA1B/image-asset.png |
| photo-daca-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255499227-YSKOA88GFNNFQ0SWXA7K/IMG_0981+%281%29.JPG |
| photo-daca-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255557529-RIETHBTVR6QYKU7SBWS0/image-asset.jpeg |
| photo-daca-3 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255575300-4NYJ221UVDHH5PKO53FX/image-asset.jpeg |
| photo-magnolia-1 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255707394-35YKYA4KECG1QWPHDA6Y/scale_2800x0x0x0_1-1484863262-49.jpg |
| photo-magnolia-2 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532256528398-CG1UCGMPYIAB9AK9CQ5R/image-asset.jpeg |
| photo-magnolia-3 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532255763302-6JAXRDHFTASCQCU9FAXK/scale_2800x0x0x0_5y-1485152887-90.jpg |
| photo-magnolia-4 | Photos | https://images.squarespace-cdn.com/content/v1/5b53d5f05cfd7950bb2ac68d/1532256554775-CKNYPXVF71VIK6B6OY1D/4.JPG |

Note: on the original Photos page, some heat-wave photos and rally photos
were interleaved. I grouped them by story for placeholder purposes; once
real images are in, we can reorder to match the original exactly.

## Facebook video posters

Facebook's embedded video player usually shows a blank/black player (no
thumbnail) to visitors who aren't logged in, so the TaiwaNYC and 中文作品
pages lay a local poster image with a play button over the video area of
each embed; clicking it reveals the real Facebook player (post text and
like counts below stay visible the whole time).

To replace the placeholder posters: open each video below, screenshot a
representative frame (16:9), save it into `/assets` under the name in the
left column (as `.jpg`/`.png`), and swap the `.svg` extension in
`build.py` / the HTML.

| Placeholder file | Page | Facebook video |
| --- | --- | --- |
| fb-taiwanyc-ep1 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/950250001977527/ |
| fb-taiwanyc-ep2 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/704495246736831/ |
| fb-taiwanyc-ep3 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/508582750011452/ |
| fb-taiwanyc-ep4 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/2618864651566880/ |
| fb-taiwanyc-ep5 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/2539421076306380/ |
| fb-taiwanyc-ep6 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/2730619417192517/ |
| fb-taiwanyc-ep7 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/358580865580597/ |
| fb-taiwanyc-ep8 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/4414730291941938/ |
| fb-taiwanyc-s2ep1 | TaiwaNyc | https://www.facebook.com/Crossing.cw/videos/2519584064988033/ |
| fb-twreporter | 中文作品 | https://www.facebook.com/twreporter/videos/3137423189888156/ |
