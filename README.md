# Split-Keyboard

<img width="1255" height="485" alt="Screenshot 2026-10-01 121230" src="https://github.com/user-attachments/assets/d56815a6-c052-4504-a009-3dc4746be0bf" />

SO I made a custom 60 % layout  Split Mechanical keyboard which has a rotor encoder at the top for brightness controlee as well . It is based on Xiao rp2040 . As it has very few pins So I had to use 2 Expanders one for each Split . The communication between 2 Splits happens with the USB-C to USB-C Connection. And We hade intricated per switch LEDs as  well . The Split Keyboard have magnets by the side SO that we could join the split and make it a big single keyboard if we want or use it as a split.  The PCB was designed on kicad and CAD was done on Fusion . firmware was written in VS-Code. It has a very compact design. The Keyboard also includes per switch LED and diodes to prevent ghosting. 

## Features

 - Based on Xiao Rp2040
 - It has A split Keyboard Design
 - had compact 60% keyboard layout
 - Per Switch LED and diode for ghosting prevention
 - Uplifted CAD Design for comfortable typing
 - Has magnets at the Edges So that the Split could be connected and used as a Simple Keyboard
   
## BOM

| Item | Price (USD) | Source |
|---|---:|---|
| PCB + Shipping + 3D Prints - Coupons | $23.14 | https://jlcpcb.com/|
| KeyCaps | $15.04 | https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/ranuw-keycap-set/ |
| Stabilizers | $10.76 | https://meckeys.com/shop/accessories/keyboard-accessories/more/glorious-goat-stabilizers/ |
| Switches (Pack of 10) × 7 | $22.10 | https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/hmx-xinhai-switch/?attribute_pa_key-switches=hmx-xinhai-45g|
| PCA9555 Expander × 2 | $6.22 | https://robu.in/product/pca9555dwr-texas-instruments-400khz-soic-24-300mil-i-o-expanders-rohs/ |
| Seeed Studio XIAO RP2040 | $5.92 | https://robu.in/product/seeed-studio-xiao-rp2040-v1-0/ |
| 1N4148W-T4 Diodes (Pack of 15) × 70 | $3.20 | https://sharvielectronics.com/product/a7-1n4007-100v-1a-silicon-rectifier-diode-sod-123fl-smd-package/|
| SK6812MINI-E | $8.10 | https://www.etstore.in/products/e9974?variant=48993209319675|
| Components Shipping | $3.30 |https://sharvielectronics.com/ / https://meckeys.com / https://robu.in |
| **Total** | **$97.78** | |



### Schematic<br><br>

<img width="971" height="611" alt="Screenshot 2026-10-08 034507" src="https://github.com/user-attachments/assets/3294479f-aae9-471a-98a1-c2b3717d91e8" />

###  PCB Design<br><br>
<img width="1237" height="467" alt="Screenshot 2026-10-08 034433" src="https://github.com/user-attachments/assets/e759d3f9-1e23-4e6d-9d55-abcd7b6409c2" />
<img width="1128" height="518" alt="Screenshot 2026-10-08 034446" src="https://github.com/user-attachments/assets/d99aac96-2bf5-4a43-ac20-910fbe564c91" />


### 3D Render <br><br>
<img width="842" height="742" alt="Screenshot 2026-10-01 121305" src="https://github.com/user-attachments/assets/2414ae61-1c4f-4f35-9a0a-d952c9eedf98" />
<img width="967" height="607" alt="Screenshot 2026-10-01 121331" src="https://github.com/user-attachments/assets/c420a905-ea25-4b83-afd2-cfac2fbdc6db" />
<img width="1255" height="485" alt="Screenshot 2026-10-01 121230" src="https://github.com/user-attachments/assets/5cff82bd-400a-4510-b56f-76cf2a06bf3c" />
