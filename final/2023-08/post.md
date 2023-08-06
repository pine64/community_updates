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
