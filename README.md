# LSST-mid-cadence
How does the typical repeat visit timescale impact flare energy estimates?


## Premise
A given star will be reobserved in the same filter after more than a week with LSST. What if we adjust the typical re-visit timescale for LSST, giving one follow-up exposue in the same filter only a few hours later?

Given a flare star light curve from *Kepler*, such as [GJ 1243](https://github.com/jradavenport/GJ1243-Flares), how would our ability to measure flare energies change with this new re-visit timescale?

To do this, take the GJ 1243 light curve (with identified flares) and draw pairs of epochs around the re-visit timescale. For all flares that are identified (criteria: at least one epoch is above some threshold above quiescence), fit the event's two epochs using the empirical flare template. *How does the average flare energy recovery go versus the re-visit timescale?*
