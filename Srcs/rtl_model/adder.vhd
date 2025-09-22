library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity adder is
    port (
        clk   : in  std_logic;
        reset : in  std_logic;
        a     : in  std_logic_vector(3 downto 0);
        b     : in  std_logic_vector(3 downto 0);
        sum   : out std_logic_vector(4 downto 0)
    );
end entity adder;

architecture rtl of adder is
begin
    process(clk)
    begin
        if rising_edge(clk) then
            if reset = '1' then
                sum <= (others => '0');
            else
                sum <= std_logic_vector(resize(unsigned(a), 5) + resize(unsigned(b), 5));
            end if;
        end if;
    end process;
end architecture rtl;
