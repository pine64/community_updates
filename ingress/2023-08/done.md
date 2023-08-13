# Submissions that were included

Quartz64/SOQuartz U-Boot upstreaming work by Kwiboo, write about the new features (load kernel from USB/NVMe, PXE) and future work (hardware RNG for KASLR). Clarify that u-boot itself still needs to be on either SPI/SD/eMMC though. Device trees/configs have been submitted and should land in U-Boot 2023.10. Also note that U-Boot can EFI boot generic aarch64 EFI images, provided their kernels are new enough for device support.

SOQuartz CM4 compatibility improvements: https://fratti.ch/articles/posts/fixing-soquartzs-support-for-orateks-tofu-board/

Talk about the new way community updates are written, who's involved, etc. Link to the repo to contribute, specify what day of the month updates are scheduled to be published now.

JF wrote about the large amount of updates that have occured over the months from the last community update to the PineTime and it's firmware InfiniTime. Things like heart rate monitoring, memory management, battery life, InfiniSim and ITD had major updates during this time. Along with Ayke starting development on their own firmware

Write about megi's rk2aw: https://xnux.eu/rk2aw/

## QuartzPro64

* Collabora's mainlining efforts on RK3588
    * AV1 hardware decoder driver
    * SATA
    * PCIe2 and PCIe3
    * PMIC -> SD card support
    * OTP
    * ADC
    * USB2
* Work still ongoing
    * USB3 (submitted)
    * cpufreq (reclocks the CPU)
    * video output
    * GPU (pancsf) https://www.collabora.com/news-and-blog/news-and-events/pancsf-a-new-drm-driver-for-mali-csf-based-gpus.html
    * mainline U-Boot

Explain what we mean by "mainlining".

Mention that this is paving the way for future RK3588-based Pine products.

## PineTime/InfiniTime
* Heart rate monitoring improvements thanks to Ceimour!
* Did you know that InfiniTime has a BLE weather service feature?
* Improved memory management
* Huge improvements to battery life (with help from Ayke!)
* InfiniSim UI update
* Improvements to ITD, the InfiniTime daemon
* Ayke is developing a brand new firmware for the PineTime
