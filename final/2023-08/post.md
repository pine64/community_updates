# August Update: Kept You Waiting, Huh?

We apologize for the lack of regular community updates during the past few months. In short, the people who usually wrote them became very busy. However, we have a new way to write and publish these updates, involving you: the community.

Let's talk about it, and about so much more of what's been happening.

N.B. Comments on the blog post need to be in English and follow our [Community Rules and Code of Conduct](https://forum.pine64.org/showthread.php?tid=13209).


## TL;DR

* Housekeeping
    * Community updates are now written collaboratively by several members of the community
    * The public is invited to contribute to the monthly update posts
* Newsflash
* Quartz64 and SOQuartz
    * U-Boot improvements thanks to Kwiboo and CounterPillow: USB, NVMe, and soon PXE
    * Improved SOQuartz CM4 baseboard compatibility
    * Improved PCIe devices compatibility
* QuartzPro64
    * What it means to "mainline" things, and why it takes time
    * Things that have been mainlined: SATA, PCIe, USB, AV1, and more!
    * Things still being worked on: cpufreq, GPU, video output


## Housekeeping

You might have been wondering why nothing new has been posted on the PINE64.org community blog in quite a few months. As was already revealed in the opening section, the reason is that previously blogs were mainly authored and edited by one person (Lukasz) and said person is extremely busy these days.

Going forward, these monthly community update posts will be written collaboratively by the community for the community. To that end, there is now a [Git repository](https://github.com/pine64/community_updates) through which this work happens. You don't need to be a good writer to contribute, you can submit links or short bullet lists and the editors will take care of the rest.

The plan is to have a post out on the 15th of every month. Whether or not this deadline will be met each month is another question, but now you can keep an eye on what's happening behind the curtains and help out if necessary.

Speaking of deadlines, this update didn't have a very long time in the proverbial oven despite the long period of silence preceding it, so it may be a little short or not cover all developments in the community equally well. Just because something is not covered in this post doesn't mean it hasn't been worked on.


## Quartz64 and SOQuartz

The RK3566 SoC that's on the Quartz64 and SOQuartz line of PINE64 devices hasn't had great mainline U-Boot support for the longest time. Technically, there was some vestigial support and an EVB (evaluation board) device tree, but it was far from optimal.

For those not in the know: U-Boot is somewhat of a mix between platform firmware ("BIOS" on your common x86 PC) and bootloader. It initializes the device's hardware, and loads a kernel (usually Linux, though not necessarily so) to which it then hands control off to.

[Kwiboo](https://github.com/Kwiboo) took it upon himself to improve the situation. Over the past few months, he's enabled U-Boot on the RK3566 and RK3568 SoCs to load kernels and device trees off USB2, USB3 and NVMe. While U-Boot itself still has to be flashed to either SPI, eMMC or SD, it can now load your kernel and device tree from a wider range of storage devices.

He also submitted device trees and board configurations to mainline U-Boot for, among other things, the Quartz64 Model A, Model B, and SOQuartz. This will land in U-Boot version 2023.10, meaning with the next stable U-Boot release, distributions no longer need to carry around their own forks (unless they want to.)

Meanwhile, [CounterPillow](https://github.com/CounterPillow) has submitted an U-Boot driver for the YT8511 ethernet PHY that's present on the Quartz64 Model A and SOQuartz. This, together with work Kwiboo is doing on a GMAC driver for the RK3566 and RK3568 SoCs, will allow users to [PXE boot operating systems over the network](https://source.denx.de/u-boot/u-boot/-/blob/master/doc/README.pxe). U-Boot's default boot flow for these boards already tries PXE, so provided you have an U-Boot flashed to one of the supported storage mediums with all the moving pieces (GMAC and PHY driver) in place, PXE will work out of the box.

There are still some small changes needed to make U-Boot initialize a random seed for KASLR on these boards. KASLR (Kernel Address Space Layout Randomization) is a security hardening technique that randomizes the locations of code in memory, making it harder for attackers to execute a successful exploit. For this to work, kernels such as Linux require that the firmware passes it an initial source of randomness. The hardware random number generator on RK3566 already has a driver in U-Boot, it just needs to be enabled for all the boards.

It's also worth pointing out that there is now improved compatibility on two fronts: CounterPillow [wrote about fixing SOQuartz compatibility with some CM4 boards](https://fratti.ch/articles/posts/fixing-soquartzs-support-for-orateks-tofu-board/), and furthermore finally submitted a small fix to Linux to improve the RK3566 and RK3568's PCIe device compatibility. There is some work left to be done, but many devices should just function as expected now.

One of the benefits of all this work is that if you've got U-Boot installed on your board, you can now simply boot generic aarch64 UEFI Linux distribution installers. Consult [the wiki for more information](https://wiki.pine64.org/wiki/Quartz64_UEFI_with_U-Boot) if this piques your interest.


## QuartzPro64

There hasn't been much talk of the QuartzPro64 on update blogs since it's been sold to developers, but that doesn't mean developers haven't been busy. The SoC used on the board, the RK3588, has been making waves in SBC communities for its performance; CounterPillow can say from personal experience that it compiles Linux kernels 7 times faster than the Quartz64's RK3566 processor.

The entirety of the work has in fact been focused on the RK3588 SoC (and associated chips, such as the RK806 PMIC), rather than the specific board PINE64 produced for developers. One of the main drivers of development are Collabora, a contracting firm specializing in open-source development. But you might be wondering what there is to even do, surely Rockchip did all the work, right?

Not quite. There's two different kinds of kernels, downstream vendor kernels and the upstream mainline kernel. The mainline Linux kernel is the Linux that sits in Linus Torvalds' git tree. Patches landing in this tree need to undergo code review by the respective subsystem maintainers, and rarely is a new driver merged without a few iterations of reviews and changes. Meanwhile, a downstream vendor kernel is (usually) forked off an LTS (Long Term Support) kernel release, and the hardware vendor then piles on patches to add hardware specific drivers and hacks. These vendor kernel change sets don't undergo the upstream kernel's review.

As you might have guessed, this often leads to less-than-ideal code being present in vendor kernels, not to forget they often don't port it to newer LTS kernel releases as they become available. So what contributors like Collabora et al do is pick up code from the vendor kernels, clean it up (or write new code entirely, as is the case with multimedia or the GPU) and submit it to mainline Linux for review and inclusion. This takes a lot of work and a lot of time, as solutions only acceptable for vendor kernels often have to be generalized into solutions that work for all sorts of systems.

Despite the odds being stacked against mainline contributors in this, significant amounts of work have already been completed. Today a mainline Linux kernel can be booted on RK3588 hardware with all 8 CPU cores (4x Cortex-A76 + 4x Cortex-A55) working, though not at their maximum frequency. Serial output works, as does the SD card thanks to new support for the often accompanying RK806 power management chip. eMMC has been working for a while, however new additions are SATA, PCIe2, PCIe3 and USB2. USB3 support is still undergoing review as of the time of writing. Smaller but still noteworthy recent additions are support for OTP (reading of one time programmable values fused into the silicon at the factory) and ADC (analog-to-digital conversion).

The most high profile recent addition would be the new driver for hardware video decoding of the AV1 video codec, of which most has been merged in Linux 6.5-rc1. This is an entirely from-scratch driver, implementing the v4l2-requests userspace API. The hardware implementation on the RK3588 processor supports decoding of up to 3840x2160 pixels in resolution video for this codec at 60 frames per second. With AV1's complexity making software decoding strenuous on CPU resources, a hardware decoder driver for this more and more widely adopted codec is essential for multimedia capabilities for future Pine products potentially based on the RK3588 System-on-Chip.

Speaking of such products, the reason why we haven't seen a consumer version of the QuartzPro64, or another RK3588 based Pine Store product, has likely been all the things missing from mainline Linux still. As already mentioned, the CPU cores with mainline Linux currently don't run at their full potential. This is because no cpufreq driver has been submitted to mainline yet, which is required for reclocking the CPU. Unlike with some green colored products however, there is no technical reason as to why reclocking wouldn't be possible, it's just a matter of someone having to do the required work to create a driver that's up to mainline's standards.

Also missing is support for video output. This is separate from the 3D GPU, as the video output processor is a Rockchip-specific hardware implementation. This means that for the time being, serial and networking are still the only ways to interact with the board.

Speaking of the 3D GPU though, the RK3588's GPU is a licensed design from Arm. Collabora is working hard on adding support for it in an open-source driver in Linux, which includes writing a new kernel driver. You can read about this driver, called pancsf, in [Collabora's blog post on the matter](https://www.collabora.com/news-and-blog/news-and-events/pancsf-a-new-drm-driver-for-mali-csf-based-gpus.html). The new architecture of the Mali-G610 GPU will allow for a fully featured Vulkan driver to be written for it in the future, something older generations of Mali GPUs had to awkwardly emulate parts of.
