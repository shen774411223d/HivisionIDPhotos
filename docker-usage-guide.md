### 构建镜像

进入根目录后执行：
`docker build -t shen774411/hivision_idphotos .`

### 构建容器

在构建镜像成功后执行：
`docker run -d -p 9003:9003 --name hivision_api shen774411/hivision_idphotos`

### 清理所有未使用的 Docker 对象，包括镜像、容器、卷和网络

`docker system prune`

---

tips: 命名时尽量使用\_下划线来分割单词
