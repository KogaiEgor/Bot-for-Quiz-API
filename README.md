Описание работы приложения

Эндпоинты для создателя тестов
    path('creator/', CreateCreator.as_view()),
    path('<int:creator_id>/uploadquiz/', UploadQuizView.as_view()),
    path('<int:creator_id>/quizlist/', GetQuizList.as_view()),
    path('<int:creator_id>/seeresults/<int:quiz>/', SeeResults.as_view()),

Эндпоинты для тестируемого
    path('<int:creator_id>/getquiz/<int:quiz>/', GetInfoAndQuiz.as_view()),
    path('<int:creator_id>/getquiz/<int:quiz>/getresult/', SaveResultView.as_view()),

Как сделать ссылки на прохождения конктреных тестов?

Следует рассмотреть deep linking https://core.telegram.org/api/links#bot-links
Похоже, что слудет указывать конкретный параметр, который, похоже, следует упомянуть в команде /start
Вероятно реализация должна быть следующей:
Бот должен иметь команду которая будет обращаться к АПИ используя url который передается в ?параметре?
Затем от туда получать всю нужную информация и преобразовывать ее в формат для теста (кнопки и вопросы)

Значит взаимодействие в общих чертах выглядит так
Со стороны создателя теста:
1) /start выбрали создателя и зарегистровались
path('creator/', CreateCreator.as_view()),
2) получили 2 кнопки: создать тест, посмотреть тесты
3) Выбрали создать тест, закинули к боту файл ворд
4) Человек прошел тест, выбрали посмотреть тесты и получили список тестов
5) Выбрали нужный, получили результаты

Комментарии:
Для пользователя создающего тесты важно отправлять свои данные каждый раз при использовании бота
Отправку данных, похоже, следует сделать в команде /start


Со стороны теструемого
1) Получили ссылку на тест (судя по всему команда /start с дополнительными параметрами) 
(бот в этот момент отправл запрос на path('<int:creator_id>/getquiz/<int:quiz>/', GetInfoAndQuiz.as_view()),)
2) Увидели тест с вопросами и кнопками в видел ответов, и прошли его
3) После прохождения теста (как это будет понимать бот пока не ясно, мб просто добавить кнопку завершить) 
бот отправляет результат на  path('<int:creator_id>/getquiz/<int:quiz>/getresult/', SaveResultView.as_view()),