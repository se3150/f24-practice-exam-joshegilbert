import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def test_describe_recharge():
    battery = Battery(100)
    battery.drain(10)
    assert battery.getCharge() == 90
    assert battery.recharge(10) == True
    assert battery.getCharge() == 100

def test_describe_drain():
    battery = Battery(100)
    battery.drain(10)
    assert battery.getCharge() == 90

def test_describe_drain_past_0():
    battery = Battery(100)
    battery.drain(200)
    assert battery.getCharge() == 0

def test_describe_recharge_past_0():
    battery = Battery(100)
    battery.drain(1000)
    assert battery.getCharge() == 0
    assert battery.recharge(10) == True
    assert battery.getCharge() == 10

def test_describe_recharge_10_times():
    for _ in range(10):
        battery = Battery(100)
        battery.drain(10)
        assert battery.getCharge() == 90
        assert battery.recharge(10) == True
        assert battery.getCharge() == 100

def test_describe_recharge_when_full():
    battery = Battery(100)
    assert battery.recharge(10000) == False
    assert battery.getCharge() == 100

def test_describe_drain_when_empty():
    battery = Battery(100)
    assert battery.drain(10000) == True
    assert battery.drain(10000) == False
    assert battery.getCharge() == 0  

def test_external_monitor_drain():
    battery = Battery(100)
    monitor = Mock()
    battery.external_monitor = monitor
    battery.drain(10)
    monitor.notify_drain.assert_called_once_with(90)

def test_external_monitor_recharge():
    battery = Battery(100)
    monitor = Mock()
    battery.external_monitor = monitor
    battery.drain(10)
    battery.recharge(10)    
    monitor.notify_recharge.assert_called_once_with(100)

def test_external_monitor_drain_and_recharge():
    battery = Battery(100)
    monitor = Mock()
    battery.external_monitor = monitor
    battery.drain(10)
    battery.recharge(10)    
    monitor.notify_drain.assert_called_once_with(90)
    monitor.notify_recharge.assert_called_once_with(100)        