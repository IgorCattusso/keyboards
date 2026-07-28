# Nexus-58 Mk.I

A fully hand-wired 58-key slightly tented split mechanical keyboard designed around the Raspberry Pi RP2040 with direct connection on both halves.
Connection type inspired by the [ScottoSplit](https://scottokeebs.com/blogs/keyboards/scottosplit).

Nexus-58 Mk.I is the first iteration of my Nexus series. My goal with this project was to create a practical, repairable, and completely custom split keyboard using readily available components and a fully 3D-printed case.


## Features

- 58-key split layout
- Hand-wired switch matrix (no PCB)
- Raspberry Pi Pico (RP2040)
- 3D-printed case
- GX20 Aviation connector with 12 Pins
- Mechanical key switches (Gateron Blue)
- Open-source hardware and firmware


## Design Philosophy

Instead of relying on a custom PCB, Nexus-58 Mk.I uses a hand-wired matrix. This makes the keyboard easier to modify, repair, and experiment with while keeping manufacturing accessible to anyone with basic soldering tools and a 3D printer.

The circular interconnect cable provides a direct connection between both halves while carrying the required signals through a single cable. This connector was chosen to reduce the cost by eliminating the need of having an MCU in each side. Also, this type of connector can be disconnected any time without worries.

A GX20 Aviation connector with 12 Pins was used on this project, but any type of connector can be used, as long as it has 12 pins to carry the signal from all 7 columns and 5 rows from the right side to the left side that has the MCU. A second MCU can be used on the right side with a P2 or USB cabe interconnecting both sides, but that would elevate the cost significantly (in my country, at least).


## Repository Contents

```text
Nexus-58-Mk-I/
├── photos/         # 3D printable models
├── software/       # Firmware source
├── stls/           # Photos and renders
└── README.md
```


## Components

Most of the components were bought in Brazil, where I live:
- Raspberry Pi Pico (RP2040): [RoboCore](https://www.robocore.net/placa-raspberry-pi/raspberry-pi-pico/)
- Pins for the Pi Pico: [RoboCore](https://www.robocore.net/conector/barra-de-40-pinos-macho-90-5-unidades/)
- Diodes: [Mercado Livre](https://www.mercadolivre.com.br/diodo-de-sinal-1n4148-kit-200-pecas/p/MLB2072206267)
- Brass screw inserts: [Mercado Livre](https://www.mercadolivre.com.br/kit-50-inserto-metalico-de-rosca-m3-impressoes-3d/up/MLBU605703878)
- Black M3 screws: [Parafuso Fácil](https://www.parafusofacil.com.br/parafuso-allen/parafuso-allen-chato/din-7991-parafuso-allen-chato-ma-3-x-6-aco-liga-classe-10-9-enegrecido-de-tempera-1/)
- GX20 Aviation connector with 12 Pins: [Elecbee](https://www.elecbee.com/en/product-detail/10sets-gx20-aviation-connector-male-and-female-one-pair-12pin-straightpanel-mount-solder-type-connector_5743)
- Mechanical key switches (Gateron Blue): [AliExpress](https://pt.aliexpress.com/item/1005005550328893.html?spm=a2g0o.order_list.order_list_main.82.1ab0caa48nc7XN&gatewayAdapt=glo2bra)
- USB cable: [Mercado Livre](https://produto.mercadolivre.com.br/MLB-5541283014-cabo-usb-carregador-celular-tipo-c-reforcado-5a-gamer-120w-_JM)
- Wires: All wires that connect both halves came from old Cat6 ethernet cables. The wires that connect rows and columns came from old coaxial cables.


## Future Revisions

The Mk.I establishes the foundation for future Nexus keyboards. Later revisions may include improved ergonomics, wireless connectivity, or additional features while maintaining compatibility where practical.


## License

See the repository's license file for licensing information.
