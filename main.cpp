#include <string>
#include <iostream>

#include "yaml-cpp/yaml.h"
#include <node.h>

namespace demo
{
  using v8::Exception;
  using v8::FunctionCallbackInfo;
  using v8::Isolate;
  using v8::Local;
  using v8::Number;
  using v8::Object;
  using v8::String;
  using v8::Value;

  void ParseYAML(const FunctionCallbackInfo<Value> &args)
  {
    Isolate *isolate = args.GetIsolate();
    String::Utf8Value str(isolate, args[0]);
    YAML::Node numbers_list = YAML::Load(std::string(*str));
    args.GetReturnValue().Set(String::NewFromUtf8(isolate, std::to_string(numbers_list.size()).c_str()).ToLocalChecked());
  }

  void Init(Local<Object> exports)
  {
    NODE_SET_METHOD(exports, "parse_yaml", ParseYAML);
  }

  NODE_MODULE(NODE_GYP_MODULE_NAME, Init)

} // namespace demo