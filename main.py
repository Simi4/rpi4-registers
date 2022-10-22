from pathlib import Path


data_dir = Path('data')


def legacy_bus_to_arm(addr: int) -> int:
    return 0xc0000000 + addr


data = [
    {
        'arm_address': 0x4c0000000,
        'regs': data_dir / 'arm_local_interrupt_regs.json',
    },
    {
        'arm_address': 0x4c0000000,
        'regs': data_dir / 'arm_mailbox_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e00b000),
        'regs': data_dir / 'armc_interrrupt_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e215000),
        'regs': data_dir / 'auxiliary_peripherals_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e007000),
        'regs': data_dir / 'dma_controller_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e101000),
        'regs': data_dir / 'general_purpose_clocks_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e200000),
        'regs': data_dir / 'gpio_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e205000),
        'regs': data_dir / 'i2c_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e203000),
        'regs': data_dir / 'pcm_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e20c000),
        'regs': data_dir / 'pwm_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e204000),
        'regs': data_dir / 'spi_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e003000),
        'regs': data_dir / 'system_timer_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e00b000),
        'regs': data_dir / 'timer_regs.json',
    },
    {
        'arm_address': legacy_bus_to_arm(0x7e201000),
        'regs': data_dir / 'uart_regs.json',
    },
]
