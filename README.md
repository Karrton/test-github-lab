# GitLab CI/CD Practice Project

Java проект с Gradle для изучения и практики GitLab CI/CD на оценку 5.

## 📋 Содержание

- [Структура проекта](#структура-проекта)
- [Требования](#требования)
- [Установка и запуск](#установка-и-запуск)
- [Git Flow организация](#git-flow-организация)
- [Работа с ветками](#работа-с-ветками)
- [Создание Merge Request](#создание-merge-request)
- [Работа с эпиками](#работа-с-эпиками)
- [CI/CD Pipeline](#cicd-pipeline)
- [Тестирование](#тестирование)

## 🏗 Структура проекта

```
gitlab-ci-practice/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/example/gitlab/
│   │           ├── Application.java           # Главный класс приложения
│   │           ├── model/
│   │           │   ├── User.java              # Модель пользователя
│   │           │   └── Task.java              # Модель задачи
│   │           └── service/
│   │               ├── UserService.java       # Сервис управления пользователями
│   │               └── TaskService.java       # Сервис управления задачами
│   └── test/
│       └── java/
│           └── com/example/gitlab/
│               ├── model/
│               │   ├── UserTest.java          # Тесты модели User
│               │   └── TaskTest.java          # Тесты модели Task
│               └── service/
│                   ├── UserServiceTest.java   # Тесты UserService
│                   └── TaskServiceTest.java   # Тесты TaskService
├── config/
│   └── checkstyle/
│       └── checkstyle.xml                     # Конфигурация Checkstyle
├── scripts/
│   └── check_team.py                          # Python скрипт для проверки MR
├── .gitlab-ci.yml                             # CI/CD конфигурация
├── build.gradle                               # Gradle конфигурация
├── settings.gradle                            # Gradle settings
└── README.md                                  # Данный файл
```

## 📦 Требования

- Java 17 или выше
- Gradle 8.0+ (или используйте Gradle Wrapper)
- Git
- GitLab аккаунт
- Python 3.8+ (для скрипта проверки)

## 🚀 Установка и запуск

### Клонирование репозитория

```bash
git clone <your-gitlab-repo-url>
cd gitlab-ci-practice
```

### Сборка проекта

```bash
# Linux/Mac
./gradlew build

# Windows
gradlew.bat build
```

### Запуск приложения

```bash
./gradlew run
```

### Запуск тестов

```bash
./gradlew test
```

### Проверка стиля кода

```bash
./gradlew checkstyleMain checkstyleTest
```

### Генерация отчета о покрытии

```bash
./gradlew jacocoTestReport
```

Отчет будет доступен в `build/reports/jacoco/test/html/index.html`

## 🌳 Git Flow организация

### Основные правила

1. **Главная ветка**: `main` - защищенная ветка, содержит только стабильный код
2. **Ветки фич**: `feature/feature-name` - для разработки новых функций
3. **Ветки багфиксов**: `bugfix/bug-name` - для исправления ошибок
4. **Ветки рефакторинга**: `refactor/refactor-name` - для улучшения кода
5. **Ветки эпиков**: `epic/epic-name` - для объединения нескольких фич

### Схема работы

```
main (защищенная)
  ↑
  └── feature/user-management (MR → main)
  └── bugfix/fix-validation (MR → main)
  └── epic/advanced-features (MR → main)
        ↑
        ├── feature/feature-1 (MR → epic/advanced-features)
        └── feature/feature-2 (MR → epic/advanced-features)
```

## 🔀 Работа с ветками

### Создание новой ветки для фичи

```bash
# Убедитесь, что вы на main и у вас последняя версия
git checkout main
git pull origin main

# Создайте новую ветку для вашей фичи
git checkout -b feature/my-awesome-feature
```

### Работа над фичей

```bash
# Делайте изменения в коде
# Добавьте файлы в staging
git add .

# Сделайте коммит с описательным сообщением
git commit -m "feat: add user authentication service"

# Отправьте ветку в GitLab
git push origin feature/my-awesome-feature
```

### Соглашения о коммитах

Используйте [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - новая функциональность
- `fix:` - исправление бага
- `refactor:` - рефакторинг кода
- `test:` - добавление тестов
- `docs:` - изменения в документации
- `style:` - форматирование кода
- `chore:` - обновление зависимостей и т.д.

Примеры:
```bash
git commit -m "feat: add Task completion feature"
git commit -m "fix: correct email validation in User model"
git commit -m "test: add unit tests for TaskService"
git commit -m "refactor: improve code structure in UserService"
```

### Синхронизация с main

```bash
# Получите последние изменения из main
git checkout main
git pull origin main

# Вернитесь в свою ветку и сделайте rebase
git checkout feature/my-awesome-feature
git rebase main

# Если возникли конфликты, разрешите их и продолжите
git add .
git rebase --continue

# Отправьте изменения (может потребоваться force push)
git push origin feature/my-awesome-feature --force-with-lease
```

## 📝 Создание Merge Request

### Через веб-интерфейс GitLab

1. Перейдите в ваш проект на GitLab
2. В меню слева выберите **Merge Requests**
3. Нажмите **New merge request**
4. Выберите source branch (вашу ветку) и target branch (обычно `main`)
5. Заполните описание MR:

```markdown
## Описание

Краткое описание того, что делает эта фича.

## Изменения

- Добавлен класс UserAuthentication
- Реализована валидация пользователей
- Написаны unit тесты (покрытие 95%)

## Тестирование

- [ ] Unit тесты проходят
- [ ] Checkstyle проходит
- [ ] Локально протестировано

## Связанные задачи

Closes #123
```

6. Нажмите **Create merge request**

### Через командную строку

```bash
# Отправьте ветку и создайте MR одной командой
git push origin feature/my-awesome-feature \
  -o merge_request.create \
  -o merge_request.target=main \
  -o merge_request.title="Add user authentication" \
  -o merge_request.description="Implementation of user authentication service"
```

### Требования к MR

1. **Размер MR** (проверяется автоматически):
   - `feature/*`: максимум 300 строк
   - `bugfix/*`: максимум 150 строк
   - `refactor/*`: максимум 400 строк
   - `epic/*`: без ограничений

2. **Обязательные элементы**:
   - Описательное название
   - Детальное описание изменений
   - Все тесты должны проходить
   - Checkstyle без ошибок
   - Код-ревью от минимум одного разработчика

3. **До мерджа**:
   - Все комментарии в ревью разрешены
   - CI/CD pipeline успешно выполнен
   - Нет конфликтов с целевой веткой

## 🎯 Работа с эпиками

Эпики используются для объединения нескольких связанных фич в одну большую функциональность.

### Создание эпика

```bash
# Создайте ветку эпика от main
git checkout main
git pull origin main
git checkout -b epic/advanced-task-management

# Отправьте ветку в GitLab
git push origin epic/advanced-task-management
```

### Создание фич в эпике

```bash
# Создайте ветки фич от ветки эпика
git checkout epic/advanced-task-management
git checkout -b feature/task-priority

# Работайте над фичей
# ...

# Создайте MR в ветку эпика (не в main!)
git push origin feature/task-priority \
  -o merge_request.create \
  -o merge_request.target=epic/advanced-task-management \
  -o merge_request.title="Add task priority feature"
```

### Структура эпика

```
epic/advanced-task-management
  ├── feature/task-priority       → MR в epic/advanced-task-management
  ├── feature/task-categories     → MR в epic/advanced-task-management
  └── feature/task-notifications  → MR в epic/advanced-task-management

После мерджа всех фич:
epic/advanced-task-management → MR в main
```

### Описание MR эпика

При создании MR эпика в main используйте следующий формат:

```markdown
## Описание эпика

Продвинутая система управления задачами с приоритетами, категориями и уведомлениями.

## Включенные фичи

- [x] feature/task-priority - Добавлена система приоритетов задач (!42)
- [x] feature/task-categories - Реализованы категории для группировки задач (!43)
- [x] feature/task-notifications - Добавлены уведомления о дедлайнах (!44)

## Общее изменение

- 450 строк кода добавлено
- 320 строк тестов
- Покрытие тестами: 92%

## Ссылки на MR

- Task Priority: !42
- Task Categories: !43
- Task Notifications: !44
```

### Пример workflow эпика

```bash
# 1. Создание эпика
git checkout main
git pull origin main
git checkout -b epic/user-profiles
git push origin epic/user-profiles

# 2. Создание первой фичи
git checkout -b feature/user-avatar
# ... работа над фичей ...
git push origin feature/user-avatar
# Создать MR: feature/user-avatar → epic/user-profiles

# 3. После одобрения, смердж feature/user-avatar в epic/user-profiles

# 4. Создание второй фичи
git checkout epic/user-profiles
git pull origin epic/user-profiles
git checkout -b feature/user-bio
# ... работа над фичей ...
git push origin feature/user-bio
# Создать MR: feature/user-bio → epic/user-profiles

# 5. После одобрения, смердж feature/user-bio в epic/user-profiles

# 6. Все фичи готовы - создаем MR эпика в main
# Создать MR: epic/user-profiles → main

# 7. После одобрения и успешного CI, мердж в main
```

## 🔄 CI/CD Pipeline

Pipeline состоит из 4 последовательных стейджей:

### Stage 1: code_quality
- Запуск Checkstyle
- Проверка стиля кода
- Проверка размера MR (через Python скрипт)
- Падает при нарушениях стиля

### Stage 2: build
- Сборка проекта через Gradle
- Создание JAR артефакта
- Артефакт хранится 1 день

### Stage 3: test
- Запуск всех unit тестов
- Генерация отчета о покрытии
- Публикация результатов тестов

### Stage 4: publish
- Публикация собранного артефакта
- Запускается только при успешных предыдущих стейджах

### Просмотр результатов pipeline

1. Перейдите в **CI/CD → Pipelines**
2. Выберите нужный pipeline
3. Просмотрите логи каждого job
4. Скачайте артефакты при необходимости

## 🧪 Тестирование

### Запуск всех тестов

```bash
./gradlew test
```

### Запуск конкретного теста

```bash
./gradlew test --tests UserServiceTest
./gradlew test --tests "UserServiceTest.shouldAddUserSuccessfully"
```

### Проверка покрытия

```bash
./gradlew jacocoTestReport
```

Откройте отчет: `build/reports/jacoco/test/html/index.html`

### Требования к покрытию

- Минимальное покрытие: 80%
- Все публичные методы должны быть покрыты тестами
- Критические пути (happy path и error cases) обязательны

## 👥 Командная работа

### Распределение задач

1. Каждый участник берет свою задачу из issue tracker
2. Создает ветку `feature/task-name`
3. Разрабатывает функциональность
4. Создает MR с детальным описанием
5. Проходит код-ревью
6. После одобрения мерджит в main

### Код-ревью

Каждый MR должен быть проверен минимум одним другим участником команды:

- Проверьте логику кода
- Убедитесь в наличии тестов
- Проверьте стиль кода
- Оставьте конструктивные комментарии
- Одобрите MR

### Разрешение конфликтов

Если возникли конфликты при мердже:

```bash
# 1. Обновите вашу ветку
git checkout feature/your-feature
git fetch origin
git rebase origin/main

# 2. Разрешите конфликты в файлах
# Отредактируйте конфликтующие файлы

# 3. Добавьте разрешенные файлы
git add .
git rebase --continue

# 4. Отправьте изменения
git push origin feature/your-feature --force-with-lease
```

## 🛠 Полезные команды

### Gradle команды

```bash
# Полная очистка и сборка
./gradlew clean build

# Запуск с логированием
./gradlew run --info

# Список всех задач
./gradlew tasks

# Проверка зависимостей
./gradlew dependencies

# Создание JAR файла
./gradlew jar
```

### Git команды

```bash
# Просмотр истории коммитов
git log --oneline --graph --all

# Просмотр изменений
git diff

# Отмена последнего коммита (сохранить изменения)
git reset --soft HEAD~1

# Просмотр статуса
git status

# Список всех веток
git branch -a

# Удаление локальной ветки
git branch -d feature/old-feature

# Удаление удаленной ветки
git push origin --delete feature/old-feature
```

## 📚 Дополнительные ресурсы

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Gradle User Guide](https://docs.gradle.org/)
- [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)
- [Checkstyle Documentation](https://checkstyle.org/)

## 🤝 Участие в проекте

1. Fork репозитория
2. Создайте ветку фичи
3. Сделайте коммиты
4. Отправьте pull request
5. Дождитесь ревью

## 📄 Лицензия

MIT License

## 👨‍💻 Авторы

- Команда разработки GitLab CI/CD Practice

---

**Примечание**: Этот проект создан для образовательных целей в рамках изучения GitLab CI/CD.
