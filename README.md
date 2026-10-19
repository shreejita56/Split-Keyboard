# Split-Keyboard

<img width="1302" height="620" alt="Screenshot 2026-10-19 152404" src="https://github.com/user-attachments/assets/359cfa7d-ca0d-49bd-8b86-a3dd2e2d7daa" />


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

<img width="1105" height="760" alt="Screenshot 2026-10-17 042426" src="https://github.com/user-attachments/assets/efb2d4dc-470a-4acd-9f57-2210eb143c98" />


###  PCB Design<br><br>
<img width="1361" height="546" alt="Screenshot 2026-10-17 042313" src="https://github.com/user-attachments/assets/e7765e6d-8581-4bac-9be1-b9fdd8655fd6" />
<img width="1261" height="573" alt="Screenshot 2026-10-17 042336" src="https://github.com/user-attachments/assets/8519a3e7-c0a7-406b-9bb5-f524d5564c28" />



### 3D Render <br><br>
<img width="1302" height="620" alt="Screenshot 2026-10-19 152404" src="https://github.com/user-attachments/assets/3878eac1-0025-43df-88ae-cd980b225005" />

<img width="1062" height="471" alt="image" src="https://github.com/user-attachments/assets/fa0df8bf-d68e-4eb1-9544-0c39b11dbce1" />
