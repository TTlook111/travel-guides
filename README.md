# travel-guides

中国旅行攻略静态网页合集，纯 HTML + 图片，无任何构建依赖，浏览器直接打开即可浏览。

## 包含站点

| 目的地 | 目录 | 页面 |
| --- | --- | --- |
| 稻城亚丁 | `daocheng-yading/` | `index.html` |
| 漠河 | `mohe-travel/` | `index.html` |
| 新疆 | `xinjiang-travel/` | `index.html` |

每个站点结构相同：`index.html` 为页面，`assets/` 存放图片等资源，全部使用相对路径引用。

## 本地预览

直接用浏览器打开对应目录下的 `index.html` 即可；也可以在仓库根目录启动任意静态服务器，例如：

```bash
python -m http.server 8000
```

然后访问 http://localhost:8000/daocheng-yading/ 等路径。

## GitHub Pages 部署

仓库 Settings → Pages → Source 选择 `Deploy from a branch`，分支选 `main` / `(root)` 后，可通过以下地址访问：

- https://ttlook111.github.io/travel-guides/daocheng-yading/
- https://ttlook111.github.io/travel-guides/mohe-travel/
- https://ttlook111.github.io/travel-guides/xinjiang-travel/
