## Feature: _pxe

<website-feature> This feature creates files meant to be booted via PXE Networkboot: .squashfs, .vmlinuz and .initrd </website-feature>

---

	Type: Flag
	Included Features: _ignite

#### Hint
Ignition Files can be used with PXE to inject information into the System at the first boot of Garden Linux. This includes Creating Users, Groups, SSH-Keys, Files, Permissions, Network Configuration...

This way Machines can be defined in a declarative way.


#

- [iPXE Documentation @ ipxe.org](https://ipxe.org/docs)
- [iPXE Script Examples @ ipxe.org](https://ipxe.org/scripting)

- [Ignition Documentation @ fedoraproject.org](https://docs.fedoraproject.org/en-US/fedora-coreos/producing-ign/#_ignition_overview)

#
