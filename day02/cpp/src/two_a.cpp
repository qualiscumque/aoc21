
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>

void read_file(std::string& data) {
  std::ifstream f;
  f.open("../../input/input.txt");
  
  if(!f.good()) {
    std::cout << "file couldn't be opened" << std::endl;
  }
  
  std::stringstream stream;
  stream << f.rdbuf(); 
  data = stream.str(); 
}


std::vector<std::string> split_string_by_newline(const std::string& str ){
  auto result = std::vector<std::string>{};
  auto ss = std::stringstream{str};

  for (std::string line; std::getline(ss, line, '\n');) {
    if(line.length() > 0)
      result.push_back(line);
  }
  return result;
}


class Pos {
 public: 
  int32_t x;
  int32_t y;
  
  Pos(const int32_t _x, const int32_t _y): x(_x), y(_y) {}
  void print(){
   std::cout << "Pos(" << x << "," << y << ")" << std::endl;    
  };
};


int main() {

  std::string data;
  read_file(data);
  std::vector<std::string> data_vec = split_string_by_newline(data);

  std::map<std::string, std::function<void(Pos&, int32_t)>> command_map = {
    {"forward", [](Pos& a, int32_t dist){a.x+=dist; }},
    {"down", [](Pos& a, int32_t dist){a.y+=dist; }},
    {"up", [](Pos& a, int32_t dist){a.y-=dist; }}
  };
    
  Pos a = Pos(0, 0);
  a.print();
 
  for(const auto& entry : data_vec) {
    std::string cmd = entry.substr(0, entry.find(" ")); 
    int32_t dist = std::atoi(entry.substr(entry.find(" "), entry.length()).c_str());
    //std::cout << cmd << "-" << dist << std::endl;
    
    command_map[cmd](a, dist);
    a.print();
    
  }
  
  std::cout << a.x * a.y << std::endl;

  
  
}
