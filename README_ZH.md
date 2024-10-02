<div align="center">
<img src="LOGO.png" alt="copying logo" width="440px" />
</div>


# copying

`copying` 是一个浏览器数据（密码|历史记录|Cookie|书签|信用卡|下载记录|localStorage|浏览器插件）的导出工具，支持全平台主流浏览器。


> 免责声明：此工具仅限于安全研究，用户承担因使用此工具而导致的所有法律和相关责任！作者不承担任何法律责任！

## 各平台浏览器支持情况

### Windows

| 浏览器                | 密码  | Cookie | 书签  | 历史记录 |
|:-------------------|:---:|:------:|:---:|:----:|
| Google Chrome      |  ✅  |   ✅    |  ✅  |  ✅   |
| Google Chrome Beta |  ✅  |   ✅    |  ✅  |  ✅   |
| Chromium           |  ✅  |   ✅    |  ✅  |  ✅   |
| Microsoft Edge     |  ✅  |   ✅    |  ✅  |  ✅   |
| 360 极速浏览器          |  ✅  |   ✅    |  ✅  |  ✅   |
| QQ                 |  ✅  |   ✅    |  ✅  |  ✅   |
| Brave              |  ✅  |   ✅    |  ✅  |  ✅   |
| Opera              |  ✅  |   ✅    |  ✅  |  ✅   |
| OperaGX            |  ✅  |   ✅    |  ✅  |  ✅   |
| Vivaldi            |  ✅  |   ✅    |  ✅  |  ✅   |
| Yandex             |  ✅  |   ✅    |  ✅  |  ✅   |
| CocCoc             |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox            |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Beta       |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Dev        |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox ESR        |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Nightly    |  ✅  |   ✅    |  ✅  |  ✅   |
| IE 浏览器             |  ❌  |   ❌    |  ❌  |  ❌   |

### MacOS

由于 MacOS 的安全性设置，基于 `Chromium` 内核浏览器解密时**需要当前用户密码**

| 浏览器                | 密码 | Cookie | 书签 | 历史记录 |
|:-------------------|:--:|:------:|:--:|:----:|
| Google Chrome      | ✅  |   ✅    | ✅  |  ✅   |
| Google Chrome Beta | ✅  |   ✅    | ✅  |  ✅   |
| Chromium           | ✅  |   ✅    | ✅  |  ✅   |
| Microsoft Edge     | ✅  |   ✅    | ✅  |  ✅   |
| Brave              | ✅  |   ✅    | ✅  |  ✅   |
| Opera              | ✅  |   ✅    | ✅  |  ✅   |
| OperaGX            | ✅  |   ✅    | ✅  |  ✅   |
| Vivaldi            | ✅  |   ✅    | ✅  |  ✅   |
| CocCoc             | ✅  |   ✅    | ✅  |  ✅   |
| Yandex             | ✅  |   ✅    | ✅  |  ✅   |
| Arc                | ✅  |   ✅    | ✅  |  ✅   |
| Firefox            | ✅  |   ✅    | ✅  |  ✅   |
| Firefox Beta       | ✅  |   ✅    | ✅  |  ✅   |
| Firefox Dev        | ✅  |   ✅    | ✅  |  ✅   |
| Firefox ESR        | ✅  |   ✅    | ✅  |  ✅   |
| Firefox Nightly    | ✅  |   ✅    | ✅  |  ✅   |
| Safari             | ❌  |   ❌    | ❌  |  ❌   |

### Linux

| 浏览器                | 密码  | Cookie | 书签  | 历史记录 |
|:-------------------|:---:|:------:|:---:|:----:|
| Google Chrome      |  ✅  |   ✅    |  ✅  |  ✅   |
| Google Chrome Beta |  ✅  |   ✅    |  ✅  |  ✅   |
| Chromium           |  ✅  |   ✅    |  ✅  |  ✅   |
| Microsoft Edge     |  ✅  |   ✅    |  ✅  |  ✅   |
| Brave              |  ✅  |   ✅    |  ✅  |  ✅   |
| Opera              |  ✅  |   ✅    |  ✅  |  ✅   |
| Vivaldi            |  ✅  |   ✅    |  ✅  |  ✅   |
| Chromium           |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox            |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Beta       |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Dev        |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox ESR        |  ✅  |   ✅    |  ✅  |  ✅   |
| Firefox Nightly    |  ✅  |   ✅    |  ✅  |  ✅   |

## 安装运行
### 安装

可下载已编译好，可直接运行的 [二进制文件](https://github.com/in179/copying/releases)

> 某些情况下，这款安全工具会被 Windows Defender 或其他杀毒软件当作病毒导致无法执行。代码已经全部开源，可自行编译。

### 从源码编译

支持 `go 1.21+` 以后版本，一些函数使用了泛型基础库

``` bash
$ git clone https://github.com/in179/copying

$ cd copying/cmd/copying

$ go build
```

### 跨平台编译

以 `macOS` 分别编译 `Windows` 和 `Linux` 程序为例：

#### Windows

``` shell
GOOS=windows GOARCH=amd64 go build
```

#### Linux

``` shell
GOOS=linux GOARCH=amd64 go build
```

### 运行
双击直接运行，也可以使用命令行调用相应的命令。

```powershell
PS C:\Users\in179\Desktop> .\copying.exe -h
NAME:
   copying - Export passwords|bookmarks|cookies|history|credit cards|download history|localStorage|extensions from browser
USAGE:
   [copying -b chrome -f json --dir results --zip]
   Export all browsing data (passwords/cookies/history/bookmarks) from browser
   Github Link: https://github.com/in179/copying
VERSION:
   0.4.6

GLOBAL OPTIONS:
   --verbose, --vv                   verbose (default: false)
   --compress, --zip                 compress result to zip (default: false)
   --browser value, -b value         available browsers: all|360|brave|chrome|chrome-beta|chromium|coccoc|dc|edge|firefox|opera|opera-gx|qq|sogou|vivaldi|yandex (default: "all")
   --results-dir value, --dir value  export dir (default: "results")
   --format value, -f value          output format: csv|json (default: "csv")
   --profile-path value, -p value    custom profile dir path, get with chrome://version
   --full-export, --full             is export full browsing data (default: true)
   --help, -h                        show help
   --version, -v                     print the version
```

举例：下面是自动扫描当前电脑上的浏览器数据，以 `JSON` 格式输出解密结果并压缩为 `zip` 文件

```powershell
PS C:\Users\in179\Desktop> .\copying.exe -b all -f json --dir results --zip

PS C:\Users\in179\Desktop> ls -l .\results\
    Directory: C:\Users\in179\Desktop\results
    
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         7/15/2024  10:55 PM          44982 results.zip
```

## Contributors

![贡献者](/CONTRIBUTORS.svg)

## Stargazers over time
[![Star History Chart](https://api.star-history.com/svg?repos=in179/copying&type=Date)](https://github.com/in179/copying)

## 404StarLink 2.0 - Galaxy
`copying` 是 404Team [星链计划2.0](https://github.com/knownsec/404StarLink2.0-Galaxy) 中的一环，如果对 copying 有任何疑问又或是想要找小伙伴交流，可以参考[星链计划的加群方式](https://github.com/knownsec/404StarLink2.0-Galaxy#community)。

<a href="https://github.com/knownsec/404StarLink2.0-Galaxy" target="_blank"><img src="https://raw.githubusercontent.com/knownsec/404StarLink-Project/master/logo.png" align="middle"/></a>

## JetBrains 开源证书支持

`copying` 项目一直以来都是在 JetBrains 公司旗下的 `GoLand` 集成开发环境中进行开发，基于 **free JetBrains Open Source license(s)** 正版免费授权，在此表达我的谢意。

<a href="https://www.jetbrains.com/?from=copying" target="_blank"><img src="https://raw.githubusercontent.com/in179/staticfiles/master/picture/jetbrains-variant-4.png" width="256" align="middle"/></a>
