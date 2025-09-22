library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity counter is
  Port (
    clk   : in  std_logic;
    rst   : in  std_logic;
    count : out std_logic_vector(7 downto 0)
  );
end counter;

architecture Behavioral of counter is
  signal cnt : unsigned(7 downto 0) := (others => '0');
begin
  process(clk, rst)
  begin
    if rst = '1' then
      cnt <= (others => '0');
    elsif rising_edge(clk) then
      cnt <= cnt + 1;
    end if;
  end process;
  count <= std_logic_vector(cnt);
end Behavioral;