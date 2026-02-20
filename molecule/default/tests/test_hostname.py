"""Testinfra tests for anxs-hostname role."""
import os


def test_hostname_file_exists(host):
    """Verify /etc/hostname exists with correct permissions."""
    f = host.file("/etc/hostname")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_hostname_file_not_empty(host):
    """Verify /etc/hostname contains a hostname."""
    f = host.file("/etc/hostname")
    assert f.exists
    content = f.content_string.strip()
    assert len(content) > 0


def test_dbus_installed(host):
    """Verify dbus package is installed."""
    assert host.package("dbus").is_installed


def test_hosts_file_exists(host):
    """Verify /etc/hosts exists."""
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.is_file


def test_hosts_has_localhost(host):
    """Verify /etc/hosts contains localhost entry."""
    f = host.file("/etc/hosts")
    assert f.contains("127.0.0.1")
    assert f.contains("localhost")
