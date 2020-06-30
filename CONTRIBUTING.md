Om du vill bidra till Enkelt är detta rätt plats att vara på! Om du vill lämna pull-request ber jag dig följa dessa riktlinjer/regler

*   Använd 4 spaces.

*   Kör unittests (projektet använder Circle-CI men försök ändå att köra test själv).

*   Använd Python3.

*   Gör alltid en ny branch med ett beskrivande men kort namn. Vi brukar använda oss av den här modellen:
`feature/kort-beskrivning` eller `fix/kort-beskrivning` samt `other/kort-beskrivning`

*   Uppdatera gärna denna fil med viktig information om det behövs.

*   Använd ' inte " i koden.

*   Följ vår uppförandekod.

*   Skriv commit-meddelanden/branch-namn, osv... på engelska eller svenska.

*   För varje bidrag du gör ska du först göra en problemraport på det här projektet och så kan du välja dig själv som "assignee" så vet andra att arbete är på gång.
Du kan sedan koppla ihop din pull-request med problemrapporten genom att i commit-meddelande skriva `Closes #[problemraportens id]`

*   Följ PEP8-standarden, t.ex. så skrivs variabler och funktions namn med `små_bokstäver_och_med_understräck` läs mer här: <https://www.python.org/dev/peps/pep-0008/>
det enklaste är att installera någonslags automatisk lösning till din textredigerare/IDE.

## Arbetsprocess

1.  Klona projektet
2.  Gör en ny _issue_ eller välj en som redan finns genom att välja dig själv som _assignee_.
3.  Gör din ändring/dina ändringar
4.  Gör en ny branch med modellen `feature/[nam-på-din-ändring]`, `fix/[namn-på-din-ändring]`, eller `other/namn-på-din-ändring`
5.  Commit, push
6.  Gör en pull request på GitHub till _master_-grenen och i beskrivningen skriv `Closes #[id till issue]`.
7.  Vänta på merge och/eller kommentarer.
