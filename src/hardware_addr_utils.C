#include <hardware_addr_utils.h>

#include <iostream>
#include <iomanip>
#include <sstream>


std::string cybermon::hw_addr_utils::to_string(const uint8_t* addr)
{
  std::ostringstream oss;
  for (int i=0; i<6; ++i)
  {
    oss << std::setw(2) << std::setfill('0') << std::hex << static_cast<const uint16_t>(addr[i]);
    if (i != 5)
    {
      oss << ':';
    }
  }
  return oss.str();
}
