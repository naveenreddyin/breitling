import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.scss'
import moment from 'moment'

export default function Home({ data }) {

  return (
    <div className="container is-fluid">
      <Head>
        <title>Breitling</title>
        <meta name="description" content="Breitling News" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Breitling News Portal
        </h1>
      </main >
      {data.count} News
      <div className={styles.footer}></div>
      {data.articles.map((item, i) => (
        <a href={item.url} key={i}>
          <div className="columns">
            <div className="column is-8">
              <p>{item.title}</p>
              <div className="columns">
                <div className="column">
                  <figure className="image is-128x128">
                    <img src={item.urlToImage} alt={item.title} />
                  </figure>
                </div>
                <div className="column">
                  <div className="columns">
                    <div className="column">
                      {item.description}
                    </div>
                  </div>
                  <div className="columns">
                    <div className="column">
                      <p>{moment(item.publishedAt).format("YYYY-MM-DD")}</p> <p>by {item.author}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </a>
      ))

      }

      <footer className={styles.footer}>

      </footer>
    </div >
  )
}

export async function getStaticProps() {
  // Fetch data from external API
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}:8080/api/news/`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}

